<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

EMMA: End-to-End Multimodal Model for Autonomous Driving

Topics include Autonomous driving, Multimodal models, Vision-language models, End-to-end driving, Motion planning, 3D object detection, Road graph prediction, Generalist models.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces EMMA, a camera-primary multimodal model that casts driving tasks such as trajectory planning, object detection, and road graph prediction into a unified language-style output space. The central value is showing how pretrained multimodal world knowledge can be co-trained with driving-specific prompts, while also exposing current limits in frame context, sensor coverage, and compute cost.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce EMMA, an End-to-end Multimodal Model for Autonomous driving. Built upon a multi-modal large language model foundation like Gemini, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planner trajectories, perception objects, and road graph elements. EMMA maximizes the utility of world knowledge from the pre-trained large language models, by representing all non-sensor inputs (e.g. navigation instructions and ego vehicle status) and outputs (e.g. trajectories and 3D locations) as natural language text. This approach allows EMMA to jointly process various driving tasks in a unified language space, and generate the outputs for each task using task-specific prompts. Empirically, we demonstrate EMMA's effectiveness by achieving state-of-the-art performance in motion planning on nuScenes as well as competitive results on the Waymo Open Motion Dataset (WOMD). EMMA also yields competitive results for camera-primary 3D object detection on the Waymo Open Dataset (WOD).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that co-training EMMA with planner trajectories, object detection, and road graph tasks yields improvements across all three domains, highlighting EMMA's potential as a generalist model for autonomous driving applications. We hope that our results will inspire research to further evolve the state of the art in autonomous driving model architectures.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving technology has made significant progress in recent years. To make autonomous vehicles a ubiquitous form of transportation, they must navigate increasingly complex real-world scenarios that require understanding rich scene context as well as sophisticated reasoning and decision-making.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Historically, autonomous driving systems employed a modular approach, consisting of specialized components for perception, mapping, prediction, and planning. While this design lends itself to easier debugging and optimization of individual modules, it poses scalability challenges due to the limited inter-module communication. In particular, the expert-designed interfaces between modules, such as the perception and behavior modules, may struggle to adapt to novel environments because they are often pre-defined based on targeted scenarios. End-to-end autonomous driving systems have recently emerged as a potential solution, directly learning to generate driving actions from sensor data. This approach eliminates the need for symbolic interfaces between modules and allows for joint optimization of driving objectives from raw sensor inputs. However, these systems are often specialized for specific driving tasks and trained on limited datasets, hindering their ability to generalize to rare or novel scenarios.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multimodal Large Language Models (MLLMs) offer a promising new paradigm for AI in autonomous driving that may help to address such challenges. This is because MLLMs, as generalist foundation models, excel in two key areas: they are trained on vast, internet-scale datasets that provide rich \"world knowledge\" beyond what is contained in common driving logs, and they demonstrate superior reasoning capabilities through techniques such as chain-of-thought reasoning that are not available in specialized driving systems. While recent efforts have explored integrating and augmenting the capabilities of existing driving systems with MLLMs, we propose to develop an autonomous driving system in which the MLLM is a first class citizen.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce the End-to-End Multimodal Model for Autonomous Driving (EMMA), built on top of a multimodal large language model, such as Gemini or PaLI without additional specialized components. Figure 1 shows the overview of the EMMA framework. EMMA accepts camera images and plain text for other non-vision inputs such as high-level driving commands and historical context. By recasting driving tasks as visual question answering (VQA) problems, EMMA leverages Gemini's pre-trained capabilities and extensive world knowledge. After EMMA is fine-tuned with driving logs from all tasks using task-specific prompts (see Figure 2 for more examples), it generates various driving outputs such as future trajectories for motion planning, perception objects, road graph elements, and scene semantics. Our experiments showcase EMMA's strong performance on several planning and perception benchmarks despite this simple design. Additionally, we find that EMMA can produce interpretable, human-readable outputs for many perception tasks such as road graph estimation, and is able to function as a generalist model that is both scalable and robust for autonomous driving.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notably, as used here and throughout the paper, the *EMMA generalist model* refers to a machine learning model that has been trained and fine-tuned on a large volume of driving data to perform a wide range of driving tasks in the autonomous driving domain.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We summarize our key findings below: EMMA exhibits strong performance in end-to-end motion planning, achieving state-of-the-art performance on public benchmarks nuScenes and competitive results on the Waymo Open Motion Dataset (WOMD). We also show that we can further improve motion planning quality with more internal training data and chain-of-thought reasoning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

EMMA demonstrates competitive results for various perception tasks including 3D object detection, road graph estimation, and scene understanding. On the camera-primary Waymo Open Dataset (WOD), EMMA achieves better precision and recall for 3D object detection than state-of-the-art methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that EMMA can function as a generalist model in the autonomous driving domain, which jointly generates the outputs for multiple driving related tasks. In particular, EMMA matches or even surpasses the performance of individually trained models when it is co-trained with motion planning, object detection, and road graph tasks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we show EMMA's capacity to reason and make decisions in complex, long-tail driving scenarios.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the remainder of this paper, Section 2 describes the detailed method of EMMA for end-to-end motion planning and generalist tasks in autonomous driving. In Section 3, we present experimental results of EMMA on public and internal datasets. Finally, we discuss related works in Sections 4.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these promising results, EMMA is not without its limitations. We discuss the limitations in-depth in the Appendix Section A.5. In particular, it faces challenges for real-world deployment due to: limitations in 3D spatial reasoning due to its inability to fuse camera inputs with LiDAR or radar, the need for realistic and computationally expensive sensor simulation to power its closed-loop evaluation, and the increased computational requirements relative to conventional models. We plan to better understand and address such challenges in future work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

While we will show EMMA can be compatible with various MLLMs such as Gemini and PaLI in our experiments, this section will focus on our main EMMA based on Gemini. We leverage the auto-regressive Gemini models that are trained to process interleaved textual and visual inputs to produce text outputs: where $\mathcal{G}$ is the Gemini model, $\mathbf{O}$ represents natural language outputs, $\mathbf{T}$ represents natural language prompts, and $\mathbf{V}$ denotes images or videos. The language output $\mathbf{O}=(o_{1},o_{2},...,o_{n})$ is generated via next-token prediction, i.e., the output probability can be represented as $P(\mathbf{O}|\mathbf{T},\mathbf{V})=\prod_{i=1}^{n}P(o_{i}|o_{<i},\mathbf{T},\mathbf{V})$ for $n$ output tokens.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Our goal is to adapt $\mathcal{G}$ for autonomous driving applications, thereby harnessing the world knowledge obtained during its pre-training phase.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

As shown in Figure 1, we map autonomous driving tasks into our Gemini-based EMMA formulation. All sensor data are represented as stitched images or videos $\mathbf{V}$; all router commands, driving context, and task-specific prompts are represented in language prompts $\mathbf{T}$; and all output tasks are presented as language outputs $\mathbf{O}$. A challenge is that many of the inputs and outputs need to capture 3D world coordinates, such as waypoint BEV (Bird's Eye View) locations $(x,y)$ for motion planning and the location and size of 3D boxes. We consider two representations: The first is direct text conversion to floating-point numbers, expressed as $\mathbf{T_{\text{coordinates}}}=\{(x_{i},y_{i})\}\approx\texttt{text}(\{(x_{i},y_{i})\})$, where the specified decimal precision depends on the distance unit and decimal points. RT-2 exemplifies this approach in robotic control.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method", "weight": 1.0} -->

The second approach uses special tokens to represent each location or action, formulated as $\mathbf{T_{\text{coordinates}}}=\{(x_{i},y_{i})\}\approx\texttt{tokenize}(\{(x_{i},y_{i})\})$, with resolution determined by the learned or manually defined discretization scheme. MotionLM leverages this method for motion forecasting. We note that the two approaches have their respective strengths and weaknesses. We opt for the text representation such that all tasks can share the same unified language representation space and they can maximally reuse the knowledge from the pre-trained weights, even though the text representation may produce more tokens than specialized tokenization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

EMMA employs a unified, end-to-end trained model to generate future trajectories for autonomous vehicles directly from sensor data. These generated trajectories are then transformed into vehicle-specific control actions such as acceleration and turning for autonomous vehicles. EMMA's end-to-end approach aims to emulate human driving behavior, focusing on two critical aspects: first, the use of navigation systems (e.g. Google Maps) for route planning and intent determination, and second, the utilization of past actions to ensure smooth, consistent driving over time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

Our model incorporates three key inputs to align with these human driving behaviors: Surround-view camera videos ($\mathbf{V}$): Provides comprehensive environment information.

<!-- chunk {"id": "body-0022", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

High-level intent command ($\mathbf{T}_{\text{intent}}$): Derived from the router, includes directives such as "go straight", "turn left", "turn right", etc.

<!-- chunk {"id": "body-0023", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

Set of historical ego status ($\mathbf{T_{\text{ego}}}$): Represented as a set of waypoint coordinates in Bird's Eye View (BEV) space, $\mathbf{T_{\text{ego}}}=\{(x_{t},y_{t})\}_{t=-1}^{-T_{h}}$ for $T_{h}$ timestamps. All waypoint coordinates are represented as plain text without specialized tokens. This can also be extended to include higher-order ego status such as velocity and acceleration.

<!-- chunk {"id": "body-0024", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

The model generates future trajectories for motion planning, represented as a set of future trajectory waypoints for the ego vehicle in the same BEV space: $\mathbf{O_{\text{trajectory}}}=\{(x_{t},y_{t})\}_{t=1}^{T_{f}}$ for future $T_{f}$ timestamps, where all output waypoints are also represnted as plain text. Putting everything together, the complete formulation is expressed as: We then fine-tune Gemini with this formulation for end-to-end planner trajectory generation, as illustrated in Figure 1. We highlight 3 characteristics of this formulation: Self-supervised: the only required supervision is the future locations of the ego vehicle. No dedicated human labels are needed.

<!-- chunk {"id": "body-0025", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

Camera-only: the only sensor input required is surround-view cameras.

<!-- chunk {"id": "body-0026", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

HD map free: no HD map is needed beyond the high-level routing information from a navigation system such as Google Maps.

<!-- chunk {"id": "body-0027", "role": "body", "section": "End-to-End Motion Planning", "weight": 1.0} -->

While we are not the first to adopt this general formulation--- conducted a thorough investigation, particularly examining the impact of including the historical ego status---our contribution lies in adapting this formulation specifically for MLLMs for autonomous driving. Our self-supervised approach exists alongside other notable methods that explore reconstruction via spatio-temporal scene decomposition, world modeling, or joint motion prediction. Beyond this self-supervised foundation, the following sections explore enhancements for EMMA by incorporating reasoning and developing generalist setups with human or auto-labels.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

Chain-of-thought prompting is a powerful tool in MLLMs that enhances reasoning capabilities and improves explainability. In EMMA, we incorporate chain-of-thought reasoning into end-to-end planner trajectory generation by asking the model to articulate its decision rationale $\mathbf{O_{\text{rationale}}}$ while predicting the final future trajectory waypoints $\mathbf{O_{\text{trajectory}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

We structure the driving rationale hierarchically, progressing from 4 types of coarse-to-fine-grained information: Scene description broadly describes the driving scenarios, including weather, day of time, traffic situations, and road conditions. We provide a concrete example for prompting Gemini. Example prompt: Assume you are an autonomous vehicle, and the images come from your front cameras. Can you describe the current scenario in terms of weather, time of the day, road environment, lane options, and your ego lane position? Example answer: The weather is clear and sunny, and it is daytime. The road is four-lane undivided street with a crosswalk in the middle. There are cars parked on both sides of the street.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

Critical objects are the on-road agents that can potentially influence the driving behavior of the ego vehicle, and we require the model to identify their precise 3D/BEV coordinates. For instance: pedestrian at \[9.01, 3.22\], vehicle at \[11.58, 0.35\].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

Behavior description of critical objects describes the current status and intent for the identified critical objects. We provide a concrete example for prompting Gemini. Example prompt: Assess the potential risks posed by the \[focused_agent\] with red bounding box. Summarize any immediate concerns that need addressing to maintain safety, paying close attention to how the objects may affect your route. Example answer: The pedestrian is currently standing on the sidewalk, looking toward the road, and maybe preparing to cross the street. The vehicle is currently ahead of me, moving in the same direction, and its future trajectory suggests it will continue straight.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

Meta driving decision includes 12 categories of high-level driving decisions, summarizing the driving plan given the previous observations. An example would be I should keep my current low speed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

We highlight that the driving rationale captions are generated using an automated tool without any additional human labels, ensuring scalability of the data generation pipeline. Specifically, we leverage off-the-shelf perception and prediction expert models to identify critical agents, and then use Gemini models with carefully designed visual and text prompts to generate scene and agent behavior descriptions. Meta driving decisions are computed using a heuristic algorithm that analyzes the ego vehicle's ground-truth trajectory.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Planning with Chain-of-Thought Reasoning", "weight": 1.0} -->

During both training and inference, the model predicts all four components of the driving rationale before predicting the future waypoints, i.e., Where $\mathbf{O_{\text{rationale}}}$ denotes an ordered text output of (R1, R2, R3, R4) for driving rationale. Empirically, we observe that the prediction order of $\mathbf{O_{\text{rationale}}}$ and $\mathbf{O_{\text{trajectory}}}$ does not result in a significant difference in quality after model convergence. This suggests that we can predict $\mathbf{O_{\text{trajectory}}}$ first and apply early stopping during inference for time-critical applications.

<!-- chunk {"id": "body-0035", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

While end-to-end motion planning is the ultimate core task, a comprehensive autonomous driving system requires additional capabilities. Specifically, it must perceive the 3D world and recognize surrounding objects, the road graph and the traffic conditions. To achieve this goal, we formulate EMMA as a generalist model capable of handling multiple driving tasks through training mixtures.

<!-- chunk {"id": "body-0036", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

Our vision-language framework represents all non-sensor inputs and outputs as plain text, providing the flexibility necessary to incorporate many other driving tasks. We employ instruction-tuning, a well-established approach in LLMs, to jointly train all tasks together with task-specific prompts included in the inputs $\mathbf{T}$ of Eq. 1. We organize these tasks into three primary categories: spatial reasoning, road graph estimation, and scene understanding.

<!-- chunk {"id": "body-0037", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

Spatial reasoning is the ability to understand, reason, and draw conclusions about objects and their relationships in space. This enables an autonomous driving system to interpret and interact with its surrounding environment for safe navigation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

Our primary focus for spatial reasoning is 3D object detection. We follow Pix2Seq and formulate the output 3D bounding boxes as $\mathbf{O}_{\text{boxes}}=\texttt{set}\{\texttt{text}(x,y,z,l,w,h,\theta,\textit{cls})\}$ where $(x,y,z)$ are the center location in the vehicle frame, $l,w,h$ are the length, width, and height of the box, $\theta$ is the heading angle, and cls is the class label in text. We convert a 7D box to text by writing floating-point numbers with two decimal places, separated by spaces between each dimension.

<!-- chunk {"id": "body-0039", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

We then represent the detection tasks using a fixed prompt $\mathbf{T_{\text{detect_3D}}}$, such as "detect every object in 3D", as follows: While $\mathbf{O_{\text{boxes}}}$ is an unordered set of boxes, the predictions from an auto-regressive language model are always ordered. We find that sorting the 3D bounding boxes by depth improves detection quality, unlike the findings in Pix2Seq.

<!-- chunk {"id": "body-0040", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

Road graph estimation focuses on identifying critical road elements for safe driving, including semantic elements (e.g., lane markings, signs) and physical properties (e.g., lane curvature). The collection of these road elements forms a road graph. For example, lane segments are represented by (a) nodes, where the lanes encounter an intersection, merge, or split and (b) edges between these nodes following the direction of traffic. The full road-graph is composed of many such polyline segments.

<!-- chunk {"id": "body-0041", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

While edges within each polyline are directional, each polyline does not necessarily have a unique order relative to the other elements. This bears similarity to object detection (e.g., ), where each box is defined by ordered attributes (top-left corner, bottom-right corner), but a relative ordering between boxes does not necessarily exist. There are several existing works that model polyline graphs with Transformers, sharing similarities with language models.

<!-- chunk {"id": "body-0042", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

Our general modeling formulation in EMMA is as follows: where $\mathbf{O_{\text{roadgraph}}}$ is a text-encoded road graph represented as waypoints, $\mathbf{T_{\text{estimate_roadgraph}}}$ is a prompt asking the model to predict the roadgrah, and $\mathbf{V}$ denotes the surrounding images.

<!-- chunk {"id": "body-0043", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

We focus specifically on predicting drivable lanes, i.e., the lanes that the ego vehicle can drive towards in the scene. These are neighboring lanes in the same traffic direction and lanes branching out from the current ego lane. To construct $\mathbf{O}_{\text{roadgraph}}$, we (a) convert lanes into sets of ordered waypoints and (b) transform these sets of waypoints into text. It is beneficial to use sample-ordered waypoints to represent both traffic direction and curvature. Just like detection, we also find that ordering lanes by approximate distance improves the prediction quality. An example of our polyline text encoding is: \"(x1,y1 and\... and xn,yn);\...\" where \"x,y\" are floating point waypoints with precision to 2 decimal places, \";\" separates polyline instances.

<!-- chunk {"id": "body-0044", "role": "body", "section": "EMMA Generalist", "weight": 1.0} -->

Scene understanding tasks test the model's understanding of the whole scene context, which can be relevant for driving. For example, roads can be temporarily obstructed due to construction, emergency situations, or other events. Detecting these blockages in a timely manner and safely navigating around them is essential for ensuring the smooth and safe operation of autonomous vehicles; however, multiple cues in the scene are required to determine if there is a blockage or not. We focus on how our model performs on this temporary blockage detection task, using the following formulation: where $\mathbf{O_{\text{temporary_blockage}}}$ is the model output signaling potential obstruction, $\mathbf{V}$ denotes the surrounding images, $\mathbf{T_{\text{road_users}}}$ denotes the all the objects on the road ahead, $\mathbf{T_{\text{temporary_blockage}}}$ is the text prompt \"is the road ahead temporarily blocked?\".

<!-- chunk {"id": "body-0045", "role": "body", "section": "Generalist Training", "weight": 1.0} -->

Our unified vision-language formulation enables the simultaneous training of multiple tasks with a single model, allowing for task-specific predictions at inference time through simple variations of the task prompt $\mathbf{T}_{\text{task}}$. This training procedure is both straightforward and flexible.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Generalist Training", "weight": 1.0} -->

For each task, we construct a dataset $\mathbf{D}_{\text{task}}$ containing $|\mathbf{D}_{\text{task}}|$ training examples. During each training iteration, we randomly sample a batch from the available datasets, with the probability of selecting an example from a specific dataset proportional to the dataset size: i.e., $|\mathbf{D}_{\text{task}}|/\sum_{t}|\mathbf{D}_{\text{t}}|$. To train for $e$ epochs, we set the total number of training iterations to $e\times\sum_{t}|\mathbf{D}_{\text{t}}|$, ensuring that the training ratio among tasks is governed by the relative dataset sizes. The optimal training ratio is influenced by several factors, including task complexity, inter-task correlations, and the degree of transferability across tasks.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Generalist Training", "weight": 1.0} -->

Our experimental results demonstrate that the generalist model, trained across multiple tasks, consistently outperforms each specialist model that is trained on a single task. This highlights the advantage of the generalist approach: enhanced knowledge transfer, improved generalization, and increased efficiency.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments are primarily based on Gemini 1.0 Nano-1, with additional results provided for a variant of EMMA based on PaLI. We first summarize the main datasets used for various experiments in Section 3.1. And then we present the results of end-to-end planner trajectory generation on two public datasets in Section 3.2. Next, we conduct experiments on our internal datasets, studying the impact of chain-of-thought and data scaling in Section 3.3. Section 3.4 focuses on 3D object detection experiments. Our co-training results for the generalist model are summarized in Section 3.5. Finally, we showcase visual results that highlight EMMA's capabilities in challenging, long-tail scenarios in Section 3.6.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

Before diving into the experimental details on how we validate EMMA, we summarize the main datasets in this section. Overall, we leverage three public datasets, nuScenes, Waymo Open Motion Dataset (WOMD) and Waymo Open Dataset (WOD). We also constructed three large-scale internal datasets for end-to-end motion planning, 3D detection and road graph estimation. We summarize the dataset sizes in Table 1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

The nuScenes dataset offers a comprehensive autonomous vehicle sensor suite for evaluation. It consists of 1,000 scenes, each spanning 20 seconds, and includes information from 6 cameras that collectively provide 360-degree coverage in the field of view.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

The WOMD dataset comprises 103k real-world urban and suburban driving scenarios, each lasting 20 seconds. These scenarios are further segmented into 1.1M examples, each representing a 9-second window: 1 second is used as input context, and the remaining 8 seconds serve as the prediction target. The dataset includes detailed map features such as traffic signal states and lane characteristics, along with agent states such as position, velocity, acceleration, and bounding boxes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

We build a large-scale internal motion planning dataset, boasting over 24 million real-world driving scenarios, each 30 seconds long. This makes it roughly 355 times larger than WOMD or any other publicly available driving dataset. To efficiently leverage this massive scale, we sample just one frame per scenario, yielding 24 million diverse training examples. This approach maximizes dataset diversity while maintaining computational efficiency.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

We also construct two separate, large-scale internal datasets for detection and road graph tasks, comprising 12 million and 8 million examples, respectively. For the detection dataset, we prioritized scenarios with diverse objects, sampling one example every 3 seconds from these scenarios. The road graph dataset, on the other hand, focuses on diverse scenarios and geo-locations, so we sample one example every 30 seconds, aligning with our motion-planning dataset.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

Lastly, we also validate the camera-based 3D object detection task on the public WOD benchmark. This benchmark offers 1150 20-second scenes, each providing meticulously synchronized and calibrated high-quality LiDAR, camera, and 3D box data from a variety of urban and suburban environments.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Summary of Datasets", "weight": 1.0} -->

Total Hours of Driving Number of Training Examples Internal Motion Planning Dataset Internal Detection Dataset Internal Roadgraph Dataset Table 1: Summary of main training dataset scales. This table details the scales of the three public datasets (nuScenes, WOMD, WOD) and three large-scale internal datasets leveraged for studying data scaling and generalist properties.

<!-- chunk {"id": "body-0056", "role": "body", "section": "End-to-End Motion Planning on Public Datasets", "weight": 1.0} -->

We conduct the end-to-end planner trajectory generation experiments on two public datasets, WOMD and the nuScenes dataset. EMMA is trained with the simplest end-to-end planner trajectory generation formulation as in Equation 2, unless specified otherwise. That is, given camera images, ego vehicle history, and driving intent, the model is asked to predict the future ego waypoints for a certain time horizon.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Driving on the Waymo Open Motion Dataset (WOMD)", "weight": 1.0} -->

EMMA† (based on PaLI) EMMA+† (based on PaLI) Table 2: End-to-end motion planning experiments on an internal planning benchmark. CoT denotes equipping with chain-of-thought reasoning (Eq. 3). EMMA+ achieves the best quality across different prediction time horizons. EMMA† and EMMA+† denotes using PaLI-X as our base model, while the default EMMA and EMMA+ use Gemini as the base model. ∗Enhanced, reproduced baselines.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Driving on the Waymo Open Motion Dataset (WOMD)", "weight": 1.0} -->

For fair comparisons, we align our settings with WOMD. Additionally, we reproduce and adapt internally enhanced versions of the state-of-the-art motion prediction models, MotionLM and Wayformer, serving as our planner baselines. These baseline models are augmented with high-level command intent as an additional input.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Driving on the Waymo Open Motion Dataset (WOMD)", "weight": 1.0} -->

As shown in Table 2 ‣ 3.2 End-to-End Motion Planning on Public Datasets ‣ 3 Experiments ‣ EMMA: End-to-End Multimodal Model for Autonomous Driving"), our model outperforms the MotionLM baseline when we train on the same dataset, with Gemini pre-trained weights. When pre-trained with our mega-scale internal dataset (denoted as EMMA+), our model outperforms both MotionLM and Wayformer. The full EFM+ (w/ CoT) surpasses the previous state-of-the-art models significantly by 13.5% at the 5s prediction horizon. We also apply the EMMA method to an open-sourced MLLM, PaLI-X, denoted as EMMA^†^ (PaLI). We show that EMMA can generalize well across different MLLMs with a large amount of training data, yielding better quality (at 1s and 3s) than previous state-of-the-art baselines.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Driving on the Waymo Open Motion Dataset (WOMD)", "weight": 1.0} -->

We note the differences in inputs between MotionLM and EMMA: MotionLM takes inputs of agent location history, agent interactions, the road graph, and traffic light states. These agent boxes are produced by specialized off-board perception models that look at both past and future observations and are trained with a large amount of carefully curated human labels, the road graph is manually generated using full run segments, and all inputs heavily use LiDAR data with superior depth estimation. In stark contrast, EMMA only takes camera images and ego vehicle history as input, without the need of any labels or additional models (besides leveraging the Gemini pre-trained weights).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Driving on the Waymo Open Motion Dataset (WOMD)", "weight": 1.0} -->

During inference, sampling a final trajectory from multiple candidates plays a critical role in the final performance. Both MotionLM and Wayformer generate 192 candidate trajectories, which are subsequently aggregated into 6 clusters using k-means clustering, resulting in 6 representative trajectories to be selected as the final output according to their probabilities. For fairness, we also sample multiple trajectories using a Top-$K$ decoding strategy, up to $K=24$. We then compute the pairwise L2 distance between all trajectories and select the one with the lowest average L2 distance as the final predicted trajectory, which can be viewed as the "median" trajectory among all the predictions. We investigate the impact of the number of sampled trajectories on ADE, as illustrated in Figure 3 ‣ 3.2 End-to-End Motion Planning on Public Datasets ‣ 3 Experiments ‣ EMMA: End-to-End Multimodal Model for Autonomous Driving"). The results highlight that sampling from multiple trajectories leads to a notable improvement in ADE, however, with diminishing return.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Driving on the nuScenes Dataset", "weight": 1.0} -->

In our experiments, we follow the standard protocol of nuScenes for planning evaluation: predict the next 3 seconds of future driving actions based on 2 seconds of historical data. We measure the planning quality with L2 errors at 1-, 2- and 3-second time horizons, aligning with established baseline methods, in particular BEV-Planner.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Driving on the nuScenes Dataset", "weight": 1.0} -->

We train and evaluate EMMA with the simplest end-to-end planner trajectory generation formulation as in Equation 2 (self-supervised, without chain-of-thought reasoning nor generalist training). As shown in Table 3, our self-supervised EMMA achieves state-of-the-art results in planning on nuScenes, outperforming all previous supervised (with intermediate perception labels and/or human labels) and self-supervised (no extra labels) methods. Under the same self-supervised setup, EMMA outperforms BEV-Planner by 17.1% in average L2 metric; even compared to OmniDrive that heavily uses intermediate perception human labels, our self-supervised EMMA improves the average L2 metric by 12.1%.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Driving on the nuScenes Dataset", "weight": 1.0} -->

Unlike in WOMD, we note that sampling multiple trajectories did not yield significant improvements. We hypothesize that this is due to nuScenes' shorter prediction time horizon (3s) in simpler driving scenarios. Thus, we report only top-1 predictions for our results.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Driving on the nuScenes Dataset", "weight": 1.0} -->

EMMA (random init) Table 3: End-to-end motion planning experiments on nuScenes. EMMA (random init) denotes models are randomly initialized; EMMA denotes models are initialized from Gemini; EMMA+ denotes models that are pre-trained on our mega-scale internal data. EMMA achieves state-of-the-art performance on the nuScenes planning benchmark, outperforming the supervised (with perception and/or human labels) prior art by 6.4% and self-supervised (no extra labels) prior art by 17.1%. ∗Ego-MLP results are taken from a reproduced version in BEV-Planner.

<!-- chunk {"id": "body-0066", "role": "body", "section": "End-to-End Motion Planning with Chain-of-Thought Reasoning on Internal Dataset", "weight": 1.0} -->

In this section, we present our studies of end-to-end planning with chain-of-thought on our internal dataset. This dataset contains 24 millions of scenarios, orders of magnitude larger than any publicly available autonomous driving dataset. The model takes in 2 seconds of history to predict the driving actions for 5 seconds into the future.

<!-- chunk {"id": "body-0067", "role": "body", "section": "End-to-End Motion Planning with Chain-of-Thought Reasoning on Internal Dataset", "weight": 1.0} -->

Table 4 presents the results of our experiments on chain-of-thought reasoning applied to end-to-end planning. By adopting the chain-of-thought formulation (Equation 3), we achieve a notable 6.7% improvement over the standard end-to-end planning approach detailed in Equation 2. We also conduct an ablation study to analyze the contributions of different rationale components. Our findings reveal that both driving meta-decision and critical object identification significantly enhance performance, contributing improvements of 3.0% and 1.5%, respectively. When these components are combined, the gains are even more substantial. Conversely, while scene description has a neutral impact on driving performance, it enhances the model's explainability. These results demonstrate that chain-of-thought reasoning can meaningfully improve driving performance, particularly when its components are carefully selected and integrated. over baseline e2e planning Table 4: Ablation study on chain-of-thought reasoning components. It improves end-to-end planning quality by up to 6.7% by combining all elements. In particular, driving meta-decision and critical objects contribute the improvements of 3.0% and 1.5%, respectively.

<!-- chunk {"id": "body-0068", "role": "body", "section": "End-to-End Motion Planning with Chain-of-Thought Reasoning on Internal Dataset", "weight": 1.0} -->

The details of each component is described in Section 2.2.

<!-- chunk {"id": "body-0069", "role": "body", "section": "End-to-End Motion Planning with Chain-of-Thought Reasoning on Internal Dataset", "weight": 1.0} -->

We also perform a series of data scaling experiments for end-to-end planning, the results of which are illustrated in Figure 4. As we train the model on a larger training set, we observe lower eval perplexities before overfitting. Our findings indicate that the driving quality of EMMA has not yet plateaued, even with the current mega-scale dataset.

<!-- chunk {"id": "body-0070", "role": "body", "section": "3D Object Detection", "weight": 1.0} -->

We validate our 3D object detection performance on the 3D camera-primary detection benchmark from the Waymo Open Dataset using the Longitudinal Error Tolerant (LET) matching. We evaluate two versions: EMMA and EMMA+, similar to earlier sections, where EMMA+ is pre-trained on the 3D detection task using our internal dataset. The quantitative results are reported on the official test set and summarized in Figure 5.

<!-- chunk {"id": "body-0071", "role": "body", "section": "3D Object Detection", "weight": 1.0} -->

Our findings show that after pre-training, EMMA+ achieves competitive performance on the benchmark. Since our model produces a set of detected boxes without individual confidence scores, we compare the precision/recall instead of LET-3D-AP, which is calculated based on the precision/recall curve. We also compare the commonly used F1-score, where EMMA's F1-score is computed using the single precision/recall and other models' F1-scores are calculated by picking the maximal F1-score on the curve (often called F1-max).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

Road graph estimation is a complex task that predicts a group of unordered polylines, each of which is represented as a sequence of waypoints. We measure the quality of road graph prediction with two metrics: lane-level precision and recall, where we define a true positive match between a predicted lane polyline and a groundtruth lane polyline if and only if their Chamfer distance is within 1 meter; and pixel-level precision and recall, where polylines are rasterized into a BEV grid with 1 meter resolution -- we then treat the BEV grid as a image and compute precision and recall based on per-pixel matching.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

As discussed in Section 2.3, this task involves several design choices. One is about the representation of road graph polylines, where our choice is to define the start and end points of each lane, with intermediate points added as needed to accurately capture the road's curvature. Another critical design choice is the construction of target label sequences used for model training. Drawing inspiration from Pix2Seq in the context of object detection, one effective design choice is to pad the targets and apply random shuffling. This technique helps the model handle unordered outputs and prevents premature termination during training.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

Polyline representation: dynamic sampling is better than fixed sampling. A simple polyline representation is to sample a fixed number of sparse control points per lane, e.g. two end points plus a fixed number of intermediate points to capture curvature. However, we find a better approach is to dynamically adjust the number of points per polyline according to the curvature and length of the lane. By keeping a consistent waypoint density rather than a consistent number of waypoints, we achieve a representation that more accurately captures the lane structure intricacies, yielding around a 40% to 90% difference in the metrics as shown in Figure 6. By adapting the waypoint density to the road geometry, particularly in areas with sharper curves or varying lane lengths, we achieve a flexible representation that more accurately captures the lane structure intricacies Polyline representation: ego-origin aligned sample intervals are better than naively aligned sample intervals. The road graph is typically stored and accessed in global coordinate frame, meaning lane origins and extensions are independent of the ego vehicle position. To improve accuracy, it is essential to adjust lane point samples to start from the ego vehicle coordinate frame origin.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

Specifically, sampling polyline points relative to the AV position (ego-origin) avoids arbitrary offsets that can arise from directly transforming points sampled in the global coordinate frame into the ego coordinate frame. This prevents a 25% to 60% drop in prediction quality.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

Target sequence construction: shuffled ordering is better than arbitrary ordering. We organize polyline targets into bins based on their endpoint distance from the ego vehicle, providing a rough global ordering. For instance, we categorize lanes into nearby lanes and those further away that serve as connecting lanes. During training, we dynamically shuffle the polylines within each distance bin to enhance the model robustness and coverage. This dynamic shuffling within each bin improves the model's ability to generalize across different lane configurations, leading to more accurate predictions.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

Target sequence construction: padding is better than non-padding. Similar to Pix2Seq, we find that padding targets to prevent early termination is highly effective. In addition to padding the total number of polyline targets, we also pad the number of points within each polyline. We use "invalid" tokens to represent padded points within polylines. Each polyline is also explicitly tagged with a final "valid" or "invalid" token to denote whether it contains any nonpadded points. This approach ensures consistent input sizes, which helps maintain the integrity of the model during training and reduces the risk of premature truncation, leading to more reliable and accurate predictions.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Road Graph Estimation", "weight": 1.0} -->

Target sequence construction: adding punctuation and other semantically redundant token improves quality. In the target sequence construction, we notice that it is beneficial to use language-like structures and punctuation to group targets (e.g., \"(x,y and x,y);\...\" instead of \"xy xy;\...\"). Additionally, explicitly including semantically redundant tokens -- such as marking padded targets as "invalid" instead of relying on implicit omissions of "valid" markers -- improves performance. This approach, incorporating punctuation and redundancy, results in a boost of up to 10% in lane-level metrics. We attribute this improvement to the language-related pre-training of Gemini. By leveraging similar structured expressions, Gemini can be more easily adapted to other tasks.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Generalist", "weight": 1.0} -->

We explore the development of the EMMA Generalist by co-training on multiple tasks and analyzing their synergies, as summarized in Table 5. For this study, we focus on three core tasks: end-to-end planning, 3D object detection, and road graph estimation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Generalist", "weight": 1.0} -->

Co-training on all three tasks yields significant improvements, with the generalist model outperforming the single-task models by up to 5.5%. We attribute these results to the complementary nature of the tasks. For example, road graph estimation becomes easier when the model can accurately identify the locations of vehicles. Similarly, driving quality is closely tied to understanding agent interactions, a skill enhanced by 3D object detection. Paring the mixture down to only two tasks still yields improvements, with certain combinations leading to greater gains than others. For instance, detection performance improves most when co-trained with driving, and road graph estimation similarly benefits most when paired with driving. This suggests the driving task plays a prominent and influential role, serving as a key contributor to overall performance improvements.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Generalist", "weight": 1.0} -->

These findings suggest that pursuing a generalist model is a promising direction for future research, with the potential for deeper insights into task synergies and performance optimization.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Generalist", "weight": 1.0} -->

Relative improvement over single task Table 5: Generalist co-training experiments. (±*) indicates standard deviation. By co-training on multiple tasks, EMMA gains a broader understanding of driving scenes, enabling it to handle various tasks at inference time, while enhancing individual task performance. Notably, certain task pairings yield greater benefits than others, suggesting these tasks are complementary. Co-training all three tasks together yields the best quality.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Visualizations", "weight": 1.0} -->

We group visual examples by scenario type: Examples (a)-(d) showcase how EMMA safely interacts with rare, unseen objects or animals on the road. Examples (e)-(f) feature EMMA navigating through construction areas. Examples (g)-(j) showcase EMMA following traffic rules at intersections with traffic lights or traffic controllers. Examples (k)-(l) highlight EMMA respecting vulnerable road users like motorcyclists.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Visualizations", "weight": 1.0} -->

Given these examples, we demonstrate the following capabilities of EMMA: Generalizability: Adapts well to diverse real-world driving scenarios across different environments and attends to objects beyond its fine-tuning categories, such as squirrels.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Visualizations", "weight": 1.0} -->

Predictive driving: Proactively adjusts to the behavior of other road users for safe and smooth driving.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Visualizations", "weight": 1.0} -->

Obstacle avoidance: Consistently adjusts trajectories to avoid obstacles, debris and blocked lanes.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Visualizations", "weight": 1.0} -->

Adaptive behavior: Safely handles complex situations like yielding, construction zones, and following traffic control signals.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Visualizations", "weight": 1.0} -->

Accurate 3D detection: Effectively identifies and tracks road agents, including vehicles, cyclists, motorcyclists, and pedestrians.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Visualizations", "weight": 1.0} -->

Reliable road graph estimation: Accurately captures road layouts and integrates them into safe trajectory planning.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Visualizations", "weight": 1.0} -->

To conclude, these scenarios highlight EMMA's capability to operate safely and efficiently in a variety of challenging and diverse driving scenarios and environments.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(a) A garbage bag appears on the freeway, so our predicted trajectory suggests to nudge slightly to the right to avoid it.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(b) A ladder appears on the freeway, and our predicted trajectory suggests to switch to the left lane to bypass it appropriately.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(c) we encounter a small squirrel on the road and our predicted trajectory instinctively slows down to avoid the animal. Note EMMA wasn’t explicitly trained to detect squirrels.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(d) A white dog appears in our lane, and our model predicts to slow down and yield. Our model also accurately detects surrounding vehicles, including those in adjacent lanes and the parking lot.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(e) As a construction zone blocks the left lanes, our predicted trajectory suggests passing through on the right, while the road graph estimation correctly identifies the blocked area.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(f) Our lane is blocked by construction cones, so our predicted trajectory suggests to move into the left lane, even though it’s in the opposite direction. EMMA captured the blockage and performed a detour.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(g) A traffic controller signals to proceed through the intersection, and our predicted trajectory aligns with the instruction.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(h) Our predicted trajectory suggests to stop as we approach an intersection with a yellow light, demonstrating cautious and safe behavior.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(i) While crossing an intersection, our predicted trajectory nudges slightly to the left due to nearby cars and a bicyclist partially occupying our lane.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(j) Our model predicts a driving trajectory to patiently wait at a red light (left). The model also accurately predicts surrounding 3D objects (middle) and road graph with lane centers (right).

<!-- chunk {"id": "body-0101", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(k) A fleet of fast-moving motorcyclists pass. The predicted trajectory suggests pausing to allow them to pass safely. Notably, motorcyclists are accurately identified by our model (middle).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Visualizations", "weight": 1.0} -->

(l) A motorbike is moving on a narrow lane at night, and yields to the right. Our predicted trajectory adjusts, guiding us to pass safely by nudging slightly to the left.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Related Works", "weight": 1.0} -->

End-to-end autonomous driving research enjoys a rich history and has evolved significantly since ALVINN employed shallow neural networks to predict control signals. The field benefited from further deep learning advancements: e.g. DAVE-2 and ChauffeurNet leveraged deeper neural architectures and incorporated sophisticated perception and motion planning modules respectively. Recent research has expanded to include multimodal inputs, multi-task learning, reinforcement learning, and distillation. Unified planning frameworks such as VAD, UniAD, PARA-Drive, and GenAD integrated planning with conventional modules in open-loop environments. More studies have been proposed to examine the robustness, safety, and transferability from synthetic environments to real-world domains. However, recent findings from AD-MLP and BEV-Planner revealed that these methods could potentially overfit to ego status despite their good performance on benchmarks. Our work revisits the simplicity of earlier end-to-end models such as ALVINN and DAVE-2, enhancing them with powerful MLLMs.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Related Works", "weight": 1.0} -->

Vision language models for autonomous driving have gained increasing interest, focusing on achieving explainable driving behavior and generalizability through end-to-end learning frameworks. DriveGPT4 and LMDrive Shao et al. utilize LLMs to explain vehicle actions and predict control signals in an iterative Q&A format. Drive Anywhere introduces patch-aligned feature extraction from MLLMs for text-based driving decision queries, while OmniDrive features a 3D vision-language model design for reasoning and planning. Other approaches use MLLMs in graph-based VQA contexts, integrate LLMs in a BEV-based planner (, or apply chain-of-thought reasoning to tackle multiple driving-related tasks. Modular architectures such as LLM-Drive leverage LLMs with object-level vector inputs for planning. In contrast, our work studies end-to-end fine-tuning of a state-of-the art MLLM for driving tasks, employing a generalist approach that emphasizes open-world driving capabilities.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Related Works", "weight": 1.0} -->

Multimodal large language models (MLLM) extend LLMs to multiple modalities, leveraging their generalizability, reasoning capabilities, and contextual understanding. Early explorations focused on specific vision-language problems or open-set object detection Liu et al.; Zareian et al.; Gu et al., while recent research has scaled up both trask diversity and model sizes for improved generalizability and few-shot capabilities. Notable examples include Flamingo, a 70B model which achieved state-of-the-art quality for multiple few-shot vision benchmarks, and CoCa a 2.1B parameter model which demonstrated state-of-the-art performance on zero-shot transfer and various downstream tasks including ImageNet classification. PaLI, at 55B parameters, achieves better performance across multiple vision and language tasks by scaling both the vision and language model components jointly. These early works demonstrate the strong performance and generalizability of MLLMs. Recent trends have seen the integration of native multi-modal inputs in LLMs, such as Gemini, GPT-4o, and Llama3-v. Notably, researchers also apply MLLMs to robotic navigation and manipulation.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Related Works", "weight": 1.0} -->

Our work explores the application of these promising new models for generalist end-to-end autonomous driving.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we present EMMA, a Gemini-powered end-to-end multimodal model for autonomous driving. It treats Gemini as a first class citizen and recasts autonomous driving tasks as vision question answering problems to fit the paradigm of MLLMs, aiming at maximizing the utility of Gemini's world knowledge and its reasoning capability equipped with chain-of-thought tools. Unlike historical cascaded systems with specialized components, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planning trajectories, perception objects, and road graph elements. All task outputs are represented as plain text and thus can be jointly processed in a unified language space through task-specific prompts. Empirical results show that EMMA achieves state-of-the-art or competitive results on multiple public and internal benchmarks and tasks, including end-to-end planning, camera-primary 3D object detection, road graph estimation, and scene understanding. We also demonstrate that a single co-trained EMMA can predict multiple tasks, while matching or even super-passing the performance of individually trained models, highlighting its potential as a generalist model for autonomous driving.
