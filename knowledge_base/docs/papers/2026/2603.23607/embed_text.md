## Introduction

Self-driving has seen substantial progress over the past decade. Perception, once the primary bottleneck, has advanced significantly through public datasets and benchmarks \[geiger2012kitti, caesar2020nuscenes, sun2020scalability\]. Today, self-driving cars are deployed across diverse geographical regions (e.g., Waymo), and perception-level generalization has seen significant improvements \[madan2024revisiting, xia2025openad\]. However, generalization in perception alone is not sufficient; decision-making in long-tail scenarios remains a major challenge. In parallel, advances in large language models (LLMs) enable contextual generalization and human-interpretable reasoning (cf. \[ke2025a\]), with language serving as a natural medium for expressing goals, constraints, and rationales.

Motivated by this gap, we introduce a dataset that couples self-driving with high-level instructions and multilingual reasoning traces, i.e., step-by-step thoughts, to accelerate progress in decision-making in long-tail scenarios. Each scenario provides a synchronized six-view video and stitched $360{^\circ}$ frames, together with human-labeled reasoning traces in English, Chinese, and Spanish. These multilingual annotations from domain experts with diverse linguistic and cultural backgrounds enable studying how reasoning styles vary with driving behavior and support cross-lingual instruction-following research.

Moreover, we evaluate multiple plausible maneuvers rather than replicating a single expert trajectory. We introduce the multi-maneuver score (MMS), a metric that rates safety, comfort, and instruction-following across multiple possible futures, similar to non-reactive simulation \[dauner2024navsim\] or pseudo-simulation \[cao2025pseudo\]. Unlike neural rendering \[agarwal2025cosmos, mousakhan2025orbis, ljungbergh2024neuroncap\], which remains promising yet artifact-prone and computationally expensive, MMS is lightweight and reproducible.

Building on the dataset and MMS, we evaluate two in-context learning (ICL) mechanisms: (i) few-shot prompting \[brown2020language\], where the model adapts from a handful of examples in the prompt and (ii) few-shot chain-of-thought (CoT) prompting \[wei2022chain\], where we append reasoning traces to our few-shot examples to guide multi‑step decision‑making. Our experiments using image- and video-based vision-language models (VLMs) show that zero‑shot planning in long‑tail scenarios is brittle, while few-shot prompting improves planning. This underscores the need for domain‑grounded reasoning.

Our main contributions are:

A dataset of long-tail driving scenarios with multi-view videos, high-level instructions, and human-labeled multilingual reasoning traces.

We measure semantic coherence between model outputs, quantifying how well the driving actions described in reasoning traces match the predicted trajectory.

The multi-maneuver score (MMS), a lightweight metric covering multiple possible maneuvers, driving comfort, and instruction following.

## Related work

### Well-established self-driving datasets

Multi-sensor datasets have driven progress in self-driving, progressing from early monocular or few‑camera recordings to $360{^\circ}$ multi-camera rigs capturing scenes across diverse geographies. However, they primarily target perception rather than planning.

KITTI \[geiger2013kitti, geiger2012kitti\] established common 2D/3D perception benchmarks, but its limited field of view and single‑city coverage constrain its diversity. nuScenes \[caesar2020nuscenes\], Waymo Open Perception \[sun2020scalability\], and Argoverse 2 \[wilson2023argoverse\] extend to multi-city captures with $360{^\circ}$ camera coverage, becoming a de‑facto standard for multi‑sensor detection, tracking, and forecasting. KITTI‑360 \[liao2021kitti360\] extends the KITTI dataset with video and panoramic coverage, supporting multi‑view methods. WayveScenes101 \[zurn2024wayvescenes101\] and MAN TruckScenes \[fent2024truckscenes\] further broaden the spectrum across vehicle types, weather, and regions, supporting platform and condition generalization but again focusing on perception rather than reasoning.

Overall, existing datasets achieve strong visual generalization across sensors and regions but offer limited insight into behavioral generalization in rare events. Our dataset complements them by integrating multi-view video, high-level instructions, and expert reasoning traces to study how models generalize in long-tail, instruction-driven decision-making.

### Benchmarks for end-to-end driving

End-to-end driving methods \[hu2023planning, jiang2023vad, sun2025sparsedrive, hwang2025emma, rowe2025poutine, sima2024drivelm\] are fully differentiable models that take raw sensor data (e.g., video, LiDAR, radar, or GNSS data) as input and output planned ego trajectories.

Despite its limitations (cf. \[li2024ego\]), benchmarking of such methods on nuScenes \[caesar2020nuscenes\] is still common (e.g., \[hwang2025emma, sun2025sparsedrive, zhang2025future\]). The corresponding evaluation protocol of Hu et al. \[hu2023planning\] computes the L2 error with respect to an expert trajectory and collision rates with other road users. Thus, the evaluation is non-reactive and considers only one maneuver as ground truth.

To consider multiple possible maneuvers, NAVSIM \[dauner2024navsim\] builds upon nuPlan \[caesar2021nuplan\] and introduces non-reactive simulation metrics. This includes metrics like progress and time to collision, but simulated ego trajectories and environments do not influence each other.

Bench2Drive \[jia2024bench2drive\] is an end-to-end driving benchmark that builds upon the CARLA simulator \[dosovitskiy2017carla\]. Its metrics like success rate and driving score are based on reactive simulation^11^1Also referred to as closed loop simulation (cf. \[jia2024bench2drive, caesar2021nuplan\]).. However, simulated sensor data exhibits a large domain gap to real data.

Most related to our work, the Waymo Open E2E benchmark \[waymo2025e2e\] evaluates end-to-end driving methods on rare long-tail scenarios, including construction zones, foreign object debris, or special vehicles. At the time of this writing, they do not provide video data, but just the camera images for the current time step. Furthermore, the benchmark data does not include reasoning traces and semantic coherence of model outputs is not evaluated.

We list further details on benchmarks and datasets for end-to-end driving in Table˜1. Figure˜1 contrasts their respective strengths and weaknesses.

nuScenes [caesar2020nuscenes]

NAVSIM [dauner2024navsim]

Bench2Drive [jia2024bench2drive]

CARLA cities (simulation)

Waymo Open E2E [waymo2025e2e]

DriveLM-Data [sima2024drivelm]

Boston, Singapore, CARLA cities

CoVLA-Dataset [arai2025covla]

Karlsruhe, Heidelberg, Mannheim, Black Forest

Table 1: Comparison of self-driving datasets used to benchmark end-to-end driving methods, VLMs, and VLAs. A half filled circle indicates that a feature is partially available. For example regarding long-tail scenarios, related work selects interesting scenarios based on variations in trajectories instead of scenario classes such as navigating a construction zone. As high-level instructions, related work provides a reduced set of {right, left, straight}.

### Reasoning mechanisms of VLMs

LLMs often solve multi-step tasks more reliably when they perform intermediate reasoning steps before producing an answer. This approach, known as chain-of-thought (CoT) \[wei2022chain\], has been extended by works that explore sampling \[wang2022self, karan2025reasoning\], tree-based search \[yao2023tree\], and sub-problem decomposition \[zhou2022least\], which typically yield higher accuracy and more consistent reasoning.

Vision-language models (VLMs) and vision-language-action models (VLAs) extend language models by conditioning on image or video inputs. VLMs generate textual outputs \[li2022blip, alayrac2022flamingo, liu2023llava\], whereas VLAs further map visual and linguistic context to executable actions \[driess2023palme, zitkovich2023rt, pi2025\]. Like LLMs, they benefit from explicit intermediate reasoning, with VLAs additionally grounding such reasoning in policies over actions \[zhao2025cot, li2025towards, mu2023embodiedgpt, wang2025vq, liu2024robomamba, zhao2025vlas\].

High-quality, domain-specific data enable task-aligned reasoning and generalization. Reinforcement learning as post-training \[openai2024o1\], fine-tuning pipelines \[deepseekai2025deepseekr1\], and semantically grounded image/video--text corpora \[deitke2024molmo\] stabilize few-shot behavior.

### Vision-language datasets for self-driving

Recent self-driving works \[sima2024drivelm, arai2025covla, wang2025omnidrive, li2024womd, chang2025langtraj\] provide natural language descriptions of traffic scenarios and actions to enhance decision-making.

DriveLM-Data \[sima2024drivelm\] extends scenarios from nuScenes and CARLA with rule-based and human Q&A labels. These labels are graph-based and cover interactions between object pairs and various tasks. Notably, Sima et al. \[sima2024drivelm\] evaluate reasoning of VLMs. However, they prompt ChatGPT-3.5 to measure semantic alignment, which is less interpretable and much more computationally expensive than our approach (see Section˜5.3).

The CoVLA-Dataset \[arai2025covla\] contains front-view videos and auto-generated behavior and reasoning captions. Arai et al. \[arai2025covla\] generate these captions using VLMs. This can lead to model collapse \[shumailov2024ai\], where training on model-generated content causes irreversible defects \[xing2025llms\].

Both DriveLM-Data and CoVLA-Dataset evaluate trajectories against single expert trajectories, overlooking the inherent multi-modality of driving. In contrast, our benchmark evaluates multiple possible maneuvers. Table˜1 provides detailed comparisons.

## Dataset

We collected our data over the course of two years, beginning in late 2023. Our recordings include urban and suburban environments, as well as highways (the main locations are listed in Table˜1). We adjusted our routes to include many construction zones and intersections. In particular, we filtered for rare events such as adverse weather conditions, road closures, and accidents. Consequently, our dataset encompasses scenarios that diverge from nominal data distributions (i.e., long-tail scenarios). Overall, our dataset contains one thousand $9\ s$-long scenarios that are divided into three splits: train ($500$), test ($400$), and validation ($100$).

### Scenarios

Figure˜2 shows the distribution of scenario types. The distribution is approximately equal across all splits.

Figure 2: Distribution of scenario types. Numbers are percentages.

In addition to specifically selected challenging scenarios (cf. Figure˜6), adverse weather, and construction zones, we use the Pareto principle to determine further long-tail data. Specifically, we use the well-established nuScenes dataset \[caesar2020nuscenes\] as reference and rank-frequency plots with a 80% cumulative frequency threshold. In nuScenes approx. 88% of the scenarios are recorded during the day, thus nighttime scenarios are long-tail data. For maneuver types, driving straight and regular turns account for approx. 90% of nuScenes. Therefore, overtaking and lane changing are part of the remaining long-tail. As an exception, we also include nominal driving at intersections to better evaluate instruction following since there are more viable trajectories than in most long-tail scenarios.

### Multi-view videos and frame-wise stitching

Table 2: Details of our video data. We provide multi-view data at a high-resolution.

Our dataset contains multi-view video data with a $360{^\circ}$ horizontal field of view (FoV) and six viewing angles (see (a) to (f) in Figure˜3). For the corresponding frames, we provide two image formats: raw and pinhole, based on a non-single viewpoint and a pinhole camera model. We optimize the pinhole parameters to create images that can be processed as ${16 \times 16}{px}$ patches (see ViTs \[dosovitskiy2020image\]).

(g) Stitched with overlap

Figure 3: Multi-view videos with frame-wise stitching. Our dataset contains multi-view videos covering a 360 ∘ FoV with partial overlap. Our stitching method creates 360 ∘ views with overlapping areas in the rear-view (see the left and right borders in (g)). We show an example from our specifically selected scenarios, in which the vehicle drives in the oncoming lane to bypass a sit-in protest by climate activists.

Furthermore, we perform frame-wise image stitching (see Figure˜3 (g)). Our stitching method introduces gradual image warping to generate $360{^\circ}$ views. Instead of applying a single homography to align overlapping image areas, our method divides each image into vertical sections. We apply a blend of the homography and the identity transformation in each section (cf. \[kinzig2022real, kinzig2024image\]).

### High-level instructions

We provide high-level driving instructions that describe the intended maneuver in each scenario. All instructions were manually annotated by domain experts. The most common command type is *drive straight on* ($45.157\, 384\, 987\, 893\, 46\ \%$), followed by turn maneuvers *turn right* ($14.527\, 845\, 036\, 319\, 61\ \%$), *turn left* ($6.174\, 334\, 140\, 435\, 835\ \%$) and use lane instructions such as *use right lane* ($7.748\, 184\, 019\, 370\, 46\ \%$) or *use left lane* ($6.537\, 530\, 266\, 343\, 826\ \%$). A distinctive feature of the dataset is the detailed formulation of overtake commands ($13.559\, 322\, 033\, 898\, 31\ \%$), which often specify both the object type and its relative position, for example *overtake truck driving on the right* or *overtake car in front*. In general, instructions can be followed throughout the scenario, but in many *specifically selected* cases this is intentionally not possible. In these scenarios, the instructed maneuver cannot be executed due to external factors such as oncoming traffic, obstacles, or the ego vehicle itself being overtaken.

Compared to purely route-based directives, such as *left*, *right*, or *straight*, used in benchmarks like Bench2Drive \[jia2024bench2drive\] or Waymo Open E2E \[waymo2025e2e\], these fine-grained textual instructions enable a more precise evaluation of instruction following and context-aware decision making.

### Reasoning traces

We ask domain experts (i.e., researchers working on self-driving) with diverse cultural backgrounds to label reasoning traces about driving actions. The experts answer five questions related to a given driving scenario and an expert-driven trajectory.

We ask the experts to answer in their mother tongue or a language they speak fluently to capture their most intuitive reasoning, resulting in reasoning traces in English, Chinese, and Spanish. Based on insights from \[deitke2024molmo\], we ask to answer the questions verbally and use Whisper \[radford2022robust\] to transcribe the responses. However, we notice that personal preference plays a role in whether answers are more verbose verbally or in writing. Therefore, we leave the decision of how to answer to each expert.

The first question is open-ended, similar to the training data of VLMs, and asks annotators to describe what they notice when observing the scenario video combined with the high-level instruction. The subsequent four questions are grounded in the expert trajectory: questions two and three address the reasons behind steering and acceleration commands during the next ${0\ s}\text{~to~}{3\ s}$, while questions four and five focus on these commands in the final two seconds (from ${3\ s}\text{~to~}{5\ s}$ into the future). Inspired by \[tas2025word\], these questions are generated using heuristics that classify acceleration commands as slight or strong acceleration, deceleration, or maintaining speed, and steering commands as slightly or sharply steering to the left/right or going straight. This structured and multilingual approach ensures comprehensive and culturally diverse explanations of driving actions. Reasoning 3.4 shows an example for a typical lane-change maneuver after an overtake maneuver.

We ask these questions to record reasoning traces about traffic scenarios and driving actions. The corresponding answers (with the actions prepended) serve as expert reasoning traces in our experiments.

## Metrics

### Semantic coherence between model outputs

We use Rocchio classification (cf. \[manning2008introduction\]) and sentence embeddings to measure semantic coherence between reasoning traces and planned trajectories.

We define semantic coherence as how well the driving actions described in the reasoning traces match the actions in the planned or predicted future trajectory. Specifically, we apply the same heuristics discussed earlier to classify the driving actions (i.e., steering and acceleration commands) of a given planned trajectory. Then, we generate embeddings of the corresponding segment of reasoning traces using EmbeddingGemma 0.3B \[vera2025embeddinggemma\]. We choose this model because, at the time of writing, it is the most computationally efficient model among the top 10 of MTEB \[muennighoff2023mteb\]. Afterwards, we perform Rocchio classification on these embeddings, comparing them to reference embeddings that represent all possible driving actions according to our taxonomy.

where $\mathbf{C}$ is the set of all classes, $\mathbf{z}$ is an embedding, ${\mathbf{μ}}_{c}$ is the reference embedding of class $c$, and $\cos{( \cdot )}$ computes the cosine similarity.

Finally, we calculate the semantic coherence score, which is the rate with which the driving action predicted from the reasoning traces $\hat{y}$ matches the driving action derived from the predicted trajectory.

Our approach is robust to the use of synonyms such as "keeping the current speed" versus "maintaining my speed", which often lead to very different scores in traditional metrics like BLEU. The classification accuracy thus indicates whether the driving actions described in the reasoning traces semantically align with those in the final planned trajectory, quantifying semantic coherence^22^2Our approach is related to recent methods for reward generation when training general purpose reasoning models \[li2025reinforcement\]. Conceptually, low semantic coherence is also related to low CoT faithfulness \[lanham2023measuring\]. Specifically, low coherence in model outputs suggests that the CoT does not accurately describe the process that led to its predictions..

### Multi-maneuver score

We agree with the recent criticism that $L_{2}$ errors with respect to expert trajectories do not capture the multi-modality of driving \[dauner2024navsim, jia2024bench2drive, caesar2021nuplan\]. Specifically, these evaluations overlook the fact that, in many scenarios, multiple maneuvers are appropriate. However, due to human reaction times,^33^3Specifically, the average driver's reaction time to surprise events is $1.5\ s$, and it takes an additional $0.2\ s$ for mechanical brakes to fully respond to pedal pressure \[green2000long\]. reactive simulation as in \[jia2024bench2drive\] is unnecessary for short time horizons in end-to-end benchmarks (e.g., $3\ s$, see Table˜1). Furthermore, neural rendering \[ljungbergh2024neuroncap, agarwal2025cosmos, gao2024vista, mousakhan2025orbis\] for realistic sensor simulation is promising, yet computationally expensive and prone to visual artifacts.

Therefore, we propose a computationally efficient evaluation that covers multiple maneuvers, comfort, potential crashes, and instruction-following. Our multi-maneuver score (MMS) ranks planned trajectories based on similarity to reference trajectories^44^4Our metric is related to rater-feedback scores \[waymo2025e2e\], but explicitly considers instruction following, comfort, and crashes. and comfort level.

jerk XOR tortuosity

jerk AND tortuosity

jerk XOR tortuosity

jerk AND tortuosity

jerk XOR tortuosity

jerk AND tortuosity

Driving off road w/o crashing

Table 3: Reference multi-maneuver scores (MMS). Our metric ranks planned trajectories based on similarity to reference trajectories of 5 categories. For the first three categories, we apply comfort penalties if the jerk or tortuosity significantly exceeds that of the reference trajectory.

For each scenario, we provide 3 reference trajectories according to the categories in Table˜3. For the expert-like trajectory category, we use the trajectory driven by an expert. For the wrong speed category, we augment the expert trajectory using state estimation and spline modifications. Specifically, we use an extended Kalman filter to smooth the expert trajectory and spline modifications to change the average speed by ${\pm 20}\ \%$. For the neglect instruction category, we manually annotate reasonable trajectories that do not follow the high-level instruction. For instance, at an intersection where the instruction is to turn right, we provide a trajectory for turning left or driving straight. For the driving off road w/o crashing category, we manually label trajectories in which the ego-vehicle partially or completely leaves the drivable area. In the crash category, we manually label rear-end collisions and crashes involving static obstacles, such as traffic signs or buildings.

We cover comfort by subtracting a comfort penalty $\text{CP} \in {\{ 0,1,2\}}$ from the maximum MMS value for each category. Specifically, we consider jerk and tortuosity relative to reference trajectories. We compute jerk using

where ${\mathbf{Y}} \in {\mathbb{R}}^{T \times 2}$ is a trajectory as temporal sequence of waypoints with x- and y-coordinates and $t \in {\{ 1,\ldots,T\}}$ indexes the temporal dimension. Moreover, we compute tortuosity using

We reduce the MMS value by 1 if the jerk of a planned trajectory is more than $44\ \%$ higher than that of a reference trajectory. Similarly, we reduce the MMS value by 1 if the tortuosity is at least $6\ \%$ higher. These relative thresholds match the ratio of the empirical standard deviation to the mean for each metric, computed for our expert trajectories using the full dataset. We apply comfort penalties to all trajectories except those associated with a crash or driving off-road (see Table˜3).

To compute the similarity between planned and reference trajectories, we leverage the miss rate metric proposed by Ettinger et al. \[ettinger2021large\]. We use their heuristic to calculate velocity-dependent lateral and longitudinal thresholds ($\lambda_{\text{lat}}$ and $\lambda_{\text{lon}}$). Specifically, we calculate a threshold-based similarity with

where $d_{\text{lat}}$ and $d_{\text{lon}}$ are lateral and longitudinal displacements between the waypoints of the planned and reference trajectories, and ${{sim}_{\text{lat}}{(d_{\text{lat}},\lambda_{\text{lat}})}} = {\max\left( 0,{1 - {{({d_{\text{lat}} - \lambda_{\text{lat}}})}/\lambda_{\text{lat}}}} \right)}$. We compute ${sim}_{\text{lon}}$ analogously using the longitudinal displacement and longitudinal threshold.

We calculate the final MMS based on 4 cases:

where $\langle \cdot, \cdot \rangle$ denotes the inner product, ${\mathbf{v}}_{\text{ref}}^{}$ is the current reference velocity, $k$ indexes the reference trajectories, $s = {{sim}\left( {\mathbf{Y}}_{\text{plan}},{\mathbf{Y}}_{\text{ref}}^{(k^{\star})} \right)}$ with $k^{\star} = {\arg{\max_{k}{{sim}\left( {\mathbf{Y}}_{\text{plan}},{\mathbf{Y}}_{\text{ref}}^{(k)} \right)}}}$, $\text{CP} \in {\{ 0,1,2\}}$ is the comfort penalty, and $\text{MMS}_{\text{ref}}$ is the score of the most similar reference trajectory (see Table˜3).

The first case in Equation˜2 assigns planned trajectories, which are inconsistent with the past trajectory, a score of 0. The second case ensures that planned trajectories, which are most similar to reference trajectories that describe crashes or driving off road (with at least moderate similarity $s \geq 0.4$), get the score of the corresponding reference trajectory. The third case assigns planned trajectories, which are most similar to reference trajectories describing good or acceptable behavior (first 3 categories in Table˜3), the score of the reference trajectory scaled by the similarity value $s$. Additionally, we ensure that the assigned MMS value is at least as high as in the unmatched fourth case. The fourth case assigns a score of 3.5 to planned trajectories, which are not matched to any reference trajectory^55^5We choose 3.5 as base MMS value to place this category between the neglect instruction and driving off road categories. We give a lower score than for the neglect instruction category, since in contrast to such reference trajectories, unmatched trajectories can neglect traffic rules. We give a higher score than for the driving off road and crash categories, since unmatched trajectories are at least consistent with the past trajectory (not case 1 in Equation 2) and unmatched trajectories are not similar to the explicit cases of driving off road or crashing (represented by the labeled reference trajectories).. As in the previous case, we also subtract comfort penalties (CP) based on jerk and tortuosity values.

## Experiments

We first compare our MMS metric to naive $L_{2}$ errors and closed-loop evaluation that requires a simulation environment. As reference for future research, we then evaluate the zero-shot and few-shot capabilities of recent VLMs on our dataset. We select general-purpose VLMs since we observe a shift in related work from domain-specific models to more general architectures (e.g., \[hwang2025emma, rowe2025poutine, zhou2025autovla\])^66^6This trend also extends to broader vision-language navigation research, see \[zhang2024visionandlanguage, windecker2025navitraceevaluatingembodiednavigation\].. To cover domain-specific models as well, we additionally evaluate end-to-end driving models without reasoning capabilities.

### Relationship between MMS, $L_{2}$ errors, and closed-loop DrivingScores

To leverage a simulation environment for this comparison, we recorded Bench2Drive \[jia2024bench2drive\] scenarios using SimLingo \[renz2025simlingo\]. We determined key frames that matched our scenario classes and label reference trajectories for expert driving, crashes, etc. (see Table˜3). We report the MMS values for the future SimLingo trajectories that were held back and average scores for longer Bench2Drive scenarios with multiple key frames. Figure˜4 shows that MMS values are significantly more correlated to the DrivingScore (DS) metric than $L_{2}$ errors are. There are few scenarios with a 0 MMS value and a 100 DS value because DS does not measure consistency with past trajectories (see first case in Equation˜2). Thus, our metric correctly returns a poor score when the car swerves heavily.

Figure 4: Relationship between MMS and L2 vs. DrivingScore (DS), with linear fits and Pearson r values (0.59 and − 0.45).

### End-to-end driving evaluation: Do models generalize to our data?

To cover both image-based and video-based open-source models, we evaluate Pixtral 12B \[agrawal2024pixtral\], Gemma 3 12B \[team2025gemma\], and Qwen3-VL 8B \[bai2025qwen3vl\]. All open-source models are instruction-tuned \[wei2022finetuned\] (i.e., trained to follow instructions by the model providers). In addition, we evaluate 3 closed-source models, Gemini 3 Pro (version: gemini-3-pro-preview), Gemini Robotics ER 1.5 \[team2025gemini\] (version: gemini-robotics-er-1.5-preview), and GPT-5 \[singh2025openai\].

We perform a zero-shot evaluation by prompting the models to plan a $5\ s$ future trajectory. As context, we provide all models with a description that they are controlling a car, the past $4\ s$ trajectory, and the high-level instruction. The Pixtral, Gemma 3, Gemini 3 Pro, Gemini Robotics ER 1.5, and GPT-5 models receive the front-view image^77^7Although challenging without calibration, recent work shows that VLMs can learn to estimate depth from images \[cai2025depthlm\] and video models generalize across different multi-camera (i.e., rig) configurations \[li2025rig3r\]. of the current time step as additional context, while the Qwen3-VL model receives the corresponding video of the past $4\ s$. Furthermore, we also evaluate UniAD \[hu2023planning\] and DMAD \[shen2025divide\] models in a zero-shot setting, both trained on nuScenes.

As few-shot evaluation, we provide the open-source VLMs with three examples, for overtaking on a highway, turning left in a suburban environment, and turning right in an urban environment. As few-shot chain-of-thought (CoT) \[wei2022chain\] evaluation, we add our expert reasoning traces (see Section˜3.4) to the few-shot examples and run the models again. As few-shot CoT kinematic evaluation, we use a simple kinematic model to generate trajectories from driving actions described in CoT reasoning traces (see Section˜5.4). We structure and optimize all prompt templates using Perplexity Pro \[PerplexityPro2025\] and include examples in the supplementary material (see Section˜7.4).

Metrics: We compute our MMS metric (see Section˜4.2) to cover multiple possible maneuvers, potential crashes, and the instruction-following capabilities of the models. Following common practice \[hu2023planning, hwang2025emma, zhou2025autovla\], we additionally compute $L_{2}$ errors with respect to the driven expert trajectory. We report both metrics for the planning horizon of $5\ s$.

Table˜4 presents the results of this experiment. In the zero-shot setting, closed-source and classic end-to-end driving models (DMAD and UniAD) outperform open-source VLMs. Gemini 3 Pro achieves the highest MMS values overall. However, the performance of open-source models significantly improves with few-shot and few-shot CoT prompting.

In general, all models perform best on the nighttime scenarios and worst on snow, intersection, and specifically selected scenarios. For snow and specifically selected scenarios, this is likely due to the challenging nature of these scenarios (cf. Figure˜6). For intersection scenarios, we hypothesize that this is due to the increased number of viable trajectories, indicating that instructions are not accurately followed. This is reinforced by the fact that most MMS values are around 4, which suggests that trajectories are not matched (see neglect instruction category in Table˜3 and Equation˜2).

Interestingly, CoT prompting worsens the results compared to plain few-shot prompting for open-source models. This is consistent with the results reported in \[sima2024drivelm, rowe2025poutine\] and may be related to differences in reasoning traces during pretraining versus our reasoning traces. Specifically, reasoning traces encountered during pre-training and instruction-tuning often focus on math \[hendrycks2021measuring\] and coding \[jain2024livecodebench\], whereas our reasoning traces explain driving actions. This is also referred to as context-memory conflicts \[xu2024knowledge\] and may be mitigated through fine-tuning on our training split.

However, using a kinematic model to convert driving actions described in CoT reasoning traces to a trajectory yields the best results for open-source models (see last block in Table˜4). Section˜5.4 connects these improvements to higher coherence between such driving actions and expert trajectories than between them and model-generated trajectories. This highlights the value of our reasoning traces about driving actions compared to providing only trajectories.

Additionally, we provide qualitative results in Figure˜5 in the supplementary material.

Pixtral 12B [agrawal2024pixtral]

Qwen3-VL 8B [bai2025qwen3vl]

Gemma 3 12B [team2025gemma]

Gemini Robotics ER 1.5 [team2025gemini]

GPT-5 [singh2025openai]

DMAD [shen2025divide]

Pixtral 12B [agrawal2024pixtral]

Qwen3-VL 8B [bai2025qwen3vl]

Gemma 3 12B [team2025gemma]

few-shot CoT English
Pixtral 12B [agrawal2024pixtral]

Qwen3-VL 8B [bai2025qwen3vl]

Gemma 3 12B [team2025gemma]

few-shot CoT Spanish
Gemma 3 12B [team2025gemma]

few-shot CoT Chinese
Gemma 3 12B [team2025gemma]

few-shot CoT kinematic
Pixtral 12B [agrawal2024pixtral]

Qwen3-VL 8B [bai2025qwen3vl]

Gemma 3 12B [team2025gemma]

Table 4: MMS scores per scenario type and L2 errors on our test set. Best scores per inference setting are bold, second best are underlined. In the zero-shot setting, closed-source and classic end-to-end driving models (UniAD and DMAD) outperform open-source VLMs. However, the performance of open-source models significantly improves with few-shot and few-shot CoT prompting.

### Semantic coherence between model outputs

We analyze the results of the previous experiment further, focusing on the reasoning traces of VLMs. Specifically, we use Rocchio classifiers to measure the coherence between the actions described in the reasoning traces and the predicted trajectory (see Section˜4.1). We parse the predicted reasoning traces from the model outputs of the inference setting with CoT prompting.

Table˜5 shows the results of this evaluation. Adapted to our format of reasoning traces (see Section˜3.4), we split the evaluation into two time intervals: ${0\ s}\text{~to~}{3\ s}$ and ${3\ s}\text{~to~}{5\ s}$. Generally, the scores for acceleration are higher than those for steering. However, we measure rather low coherence overall, with average scores ranging from $0.27\text{~to~}0.51$. In other words, in ${73\ \%}\text{~to~}{49\ \%}$ of the scenarios, the actions described in the reasoning trace do not match the planned trajectory. Thus, the models frequently either hallucinate \[huang2025survey\] reasoning traces or predict unreasonable trajectories. This is likely due to the domain gap between the pre-training data and our dataset, which highlights a challenge in improving the generalization of such models in future work.

Gemma3 12B [team2025gemma]

Qwen3-VL 8B [bai2025qwen3vl]

Pixtral 12B [agrawal2024pixtral]

Table 5: Semantic coherence of model outputs. The scores quantify how well the actions (acceleration and steering) described in reasoning traces (i.e., intermediate outputs) match the planned future trajectories (i.e., final model outputs).

### From low semantic coherence to improved planning

Section˜5.3 highlights that intermediate model outputs (i.e., reasoning traces) and final model outputs (i.e., planned trajectories) are rarely coherent. Thus, we further analyze the predictions of Gemma 3 and find that the driving actions described in the intermediate reasoning traces match the expert trajectories better than the final planned trajectories.

Building on this, we improve the few-shot CoT inference by adding a simple kinematic model. Specifically, we let the model predict the driving actions and reasons for the two time intervals (${0\ s}\text{~to~}{3\ s}$ and ${3\ s}\text{~to~}{5\ s}$) as before. These driving actions are mapped to 10 discrete acceleration values and steering angles, each of which is speed-dependent (see Table˜6). Afterwards, we use a kinematic bicycle model (cf. \[kong2015kinematic\]) to generate a planned future trajectory from the driving actions and the past trajectory. The last block in Table˜4 shows that this inference configuration significantly improves the results and yields the highest MMS values. This supports the finding that model generated reasoning traces include driving actions that represent good or acceptable driving behavior (see first 3 categories in Table˜3).

## Conclusion and discussion

Real-world driving is inherently long-tailed, requiring algorithms and systems that remain robust and reliable in rare situations. VLMs and VLAs offer a promising avenue for decision-making in such scenarios, given they are grounded in domain data and supported by in-context learning.

We provide long-tail scenarios with multi-view videos, high-level instructions, and human-labeled reasoning traces for self-driving. We evaluated several models, measuring the semantic coherence between their outputs and how well they capture the multi-modality of driving. The results show consistent improvements over zero-shot baselines when the models are prompted with our few-shot examples or few-shot CoT.

Our dataset supports several research directions. RL‑based fine‑tuning \[deepseekai2025deepseekr1, openai2024o1\] to jointly optimize motion trajectories and reasoning traces is a natural next step. Another direction is to examine whether pre-training or fine-tuning on particular reasoning styles or languages improves performance \[wang2025scaling\]. Beyond VLMs and VLAs, our dataset also enables evaluating world models (especially with text decoders such as VL-JEPA \[chen2025vl\]), opening a further avenue for assessing whether internal world representations lead to more grounded reasoning in long-tail scenarios. Moreover, our dataset supports evaluating how human-like the reasoning traces of AI models are by comparing them to expert reasoning traces. Finally, while scaling models and data will likely continue to improve generalization and accuracy, interpretability will remain central. Understanding the mechanisms that lead to actions enables not only transparency but also improved debugging and model development.
