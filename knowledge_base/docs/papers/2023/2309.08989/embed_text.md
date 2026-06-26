## Introduction

Accurately predicting the motion of road users is essential in autonomous driving systems. This predictive capability provides the planner with a forward-looking perspective on potential movements, thereby enhancing safety measures. While learning-based motion prediction has become increasingly popular in recent research, the exploration of pretraining and self-supervised learning within this field remains relatively limited.

The technique of random masking has demonstrated its effectiveness in various fields, such as natural language processing (NLP) and computer vision (CV), as evidenced by models like BERT and Masked Autoencoders in conjunction with Vision Transformers (ViT ). Random masking involves concealing a portion of the data (masking), and then tasking the neural network with predicting the hidden elements, thereby creating a nontrivial and beneficial self-supervisory task. This method employs an asymmetric encoder-decoder architecture, which has proven to be particularly powerful regarding training speed with large datasets. Furthermore, it has demonstrated exceptional performance in transfer learning, particularly in tasks related to image processing.

Figure 1: Random Masking for Motion Data. We treat time-sequential data as one dimension and all agents in the scenario as another, with each cell representing the high-dimensional features of an agent (including position, heading, agent type, agent shape, etc.). Left: Motion prediction is a special case where all future timesteps are masked (shown in blue). Right: We apply random masking to a scenario, hiding patches for random agents and random time steps for pretraining. Ego stands for the ego autonomous vehicle.

Inspired by SceneTransformer, the motion prediction task is linked with a mask on the future time sequential data of road users. As depicted in Fig. 1, the data for all agents can be represented as a grid, with time and agent forming the two axes. In this context, motion prediction becomes a unique task wherein future states are masked. This leads us to the natural question: Could random mask pretraining be effectively applied to general motion tasks as well? These tasks include motion prediction (marginal, conditional, etc.), occlusion handling, and others. We introduce a straightforward yet potent framework for random masking pretraining (RMP) for motion tasks. Our RMP selectively conceals motion patches, allowing the random mask to capture spatial and social correlations among all agents in a given scenario. This universal framework can be readily integrated into numerous motion prediction methodologies. In this paper, we demonstrate its adaptability by incorporating it into several state-of-the-art models, including Autobots and Hivt.

We assess the impact of pretraining on performing three different tasks: motion prediction, conditional motion prediction, and occlusion handling. In case of conditional motion prediction, not only is the historical information of all agents provided, but also the desired trajectory of the ego vehicle. The network then endeavors to predict the trajectories of all other agents.

In addition to classic motion prediction, we also treat occlusion handling as a separate task to evaluate our proposed framework. In real-world scenarios, occlusions are a common occurrence where one or more agents are partially or entirely obscured from view. Under such circumstances, predicting the motion of the occluded agents become a complex task that can significantly influence the overall performance of the autonomous driving system, especially with occlusions happening over short distances. This is a nontrivial issue that has often not been specifically focused on in practice. For agents whose historical trajectories are partially or heavily occluded, we evaluate the performance of the current state-of-the-art networks with and without masking pretraining in an object-based manner.

Our experimental results indicate that motion prediction benefits from transfer learning for generalization and random masking. Our framework demonstrates effective performance on the Argoverse and NuScenes datasets. Our code will be publicly accessible at In this paper, we make the following contributions: We introduce a pretraining framework for a range of motion-related tasks.

We design experiments to validate the effectiveness of random masking.

We highlight that occlusion handling remains a challenge for current state-of-the-art methods and demonstrate that our pretraining method enhances performance in this area.

## Related Work

### II-A Motion Prediction

Motion prediction has recently been explored rapidly with large open datasets and public benchmarks. Early approaches drew inspiration from successful computer vision techniques, where map and agents' historical trajectories were rasterized into images using specific color encoding. However, rasterization carries certain limitations, such as the challenge of selecting an optimal Field-Of-View (FOV) due to the high computational cost of high-resolution imaging and the potential for long-distance information loss. An alternative approach to these challenges is using sparse vectors and polygons, as exemplified by VectorNet. Other network architectures that have been explored include Graph Neural Networks and Transformers. The outputs of these representations vary: some generate a set of point trajectories in an end-to-end manner, while others generate top K trajectory samples from anchors, heatmaps, or kinematic models. Owing to its adaptability, our proposed framework can be effectively incorporated into many of these methods.

### II-B Self-supervised Learning

Self-supervised learning methods have garnered substantial interest across various fields, such as NLP and CV. These methods leverage different tasks to initialize network weights in the pretraining phase. For instance, contrastive learning designs tasks that distinguish between similarities and dissimilarities, utilizing both original data samples and their augmented counterparts. The Masked Autoencoder, proposed , uses a masking encoder to reconstruct missing pixels in images during the pretraining phase, resulting in better performance and a training speed that is four times faster than training from scratch. This technique has inspired applications in a variety of domains, such as video, 3D point clouds, and visual reinforcement learning in robotics. Self-supervised learning for motion prediction in autonomous driving remains largely unexplored. However, in the past year, a few studies have started investigating this area. Prarthana et al. propose a suite of four pretraining tasks, including lane masking, intersection distance calculation, maneuver classification, and success/failure classification. The work most similar to ours is the recent archive preprint which shows results similar to our own on one of the tasks we tested (prediction). Our work here was developed independently to.

### II-C Conditional Motion Prediction

Compared to standard motion prediction, conditional motion prediction offers additional information by incorporating specific conditions, such as the intended path of the ego vehicle. For example, the work presented in generates predictions based on hypothetical 'what-if' interactions among road users and lanes. In this way, although their targeted task closely resembles standard motion prediction, it extends the context by incorporating speculative interaction scenarios. Additionally, studies like and adopt a two-step approach in their prediction methodology by first predicting the destination positions, which are then used as conditions for predicting full trajectories. This effectively transforms the prediction task into a conditional one, where the trajectories are predicated on hypothesized destinations.

### II-D Occlusion Handling

Handling occlusions in motion prediction is crucial for enhancing the robustness and reliability of autonomous driving systems. A widely adopted representation called Occupancy Grid Map (OGM) captures the spatial arrangement of obstacles and free space where each grid cell represents the estimated probability of an agent's presence within. Predicting future OGM allows the formation of occluded areas, thus offering a more comprehensive understanding of the environment. Nevertheless, these approaches based on OGM can be computationally expensive, particularly for high-resolution, large, and complex environments. For object-based methods, there has been limited work due to the lack of motion prediction datasets that annotate occluded objects. Most datasets are primarily collected from the ego vehicle's perspective. To help mitigate this, we have post-processed the INTERACTION dataset, which was captured from bird's-eye-view drones. This has allowed us to estimate occlusion labels for objects, and we openly share the resulting post-processed dataset for further research in this area.

## Problem Formulation

Consider a scenario including $N$ agents' trajectories $A$ over $T$ timestamps, denoted as $A_{i} \in {\mathbb{R}}^{T \times D_{agent}}$, where $i \in {\lbrack 1,N\rbrack}$, along with the surrounding road topology ${Map} \in {\mathbb{R}}^{S \times P \times D_{road}}$. Here, $S$ represents the number of road segments, $P$ denotes the number of points within a segment, and $D$ signifies the vector feature dimension that includes position coordinates $x,y$ and the validity mask for both $D_{agent}$ and $D_{road}$. If yaw angle, velocity and agent size of the agents are provided in the dataset, they are also added into the feature $D$.

In the context of motion prediction, we are provided with the historical trajectory $A_{history} \in {\mathbb{R}}^{T_{obs} \times D_{agent}}$, where $T_{obs}$ signifies the observed historical timestamps, and our task is to predict the future trajectory $A_{future} \in {\mathbb{R}}^{T_{fut} \times D_{agent}}$.

Here, it is worth mentioning that occlusion can complicate this task, as $A_{history}$ may contain many occluded objects with unknown states. In the case of conditional motion prediction, however, additional elements are taken into account. In particular, the historical information is supplemented with the ego vehicle's anticipated future route path $A_{ego} \in {\mathbb{R}}^{T_{fut} \times D_{agent}}$ (where $i$ equals to index of ego vehicle), which forms part of the input.

Figure 2: The pretraining framework. In the first pretrain phase, all agents’ information including the history and future time are concatenated together. Next, random masking is applied. Then, given incomplete information about agents’ positions with time (in grey), where some positions are randomly masked (in blue), the network trains to fill in the missing positions. In the fine-tuning phase, there are three tasks that correspond to three special masking cases. Once trained, the pretrained encoder is used for different tasks.

## Methodology

In this section, we outline the strategy employed in our study. Fig. 2 provides an illustration of the complete training framework, and the specifics of the random masking application are outlined in the following sub-sections.

Figure 3: Different mask sampling strategies: (a) random pointwise masking, (b) random patchwise masking for random agents, (c) random masking in time. All show 75% masking in total (in blue) and the remaining data (in grey) will be fed into the network.

(a) Different mask ratios and profiles where 75% pointwise mask performs best.

(b) With or without frozen pretrained encoder.

(c) Different number of encoder blocks.

TABLE I: Ablation experiments on our pretrain framework with the Autobot model on Argoverse validation dataset. We have evaluated the influences of different mask sampling strategies, finetuning with or without the frozen pretrained encoder weights, and also the encoder size. w/[P] represents the method with our random masking pretraining. The default setting is highlighted in grey.

### IV-A Network

Our approach is an extension of the masked autoencoder for time-sequential trajectory data and aims to provide a simple, yet effective framework that is applicable to many motion prediction methodologies with minimal domain-specific knowledge required.

The framework can accommodate many network architectures in a two-stage process. In the first stage, different masking strategies are applied to all timestamps including the history and future timestamps, and for all agents. Given incomplete waypoints, the model tries to predict $K$ possible completed trajectories. Therefore, we don't need to change the loss function from the original methods. In the second fine-tuning stage, the network combines the pretrained encoder and the task-specific decoder.

Our method tests on two networks -Autobot-Joint and HiVT. Autobot-Joint is a transformer-based network that uses an axial attention mechanism to learn the temporal and spatial correlations among agents and road topology. Hivt models the local and global context in a translation and rotation invariant transformer network.

### IV-B Masking

By changing the validity mask within the input, the pretraining task can easily be switched among trajectory completion (pretraining task), motion prediction, and conditional prediction. The mask defines which parts can be seen by the network. For the unseen parts, we further set them as zeros to guarantee a clean input for the network.

The random masking pretraining incorporates pointwise, patchwise, and time-based strategies, as illustrated in Fig. 3, each serving a distinct purpose. The pointwise approach (Fig. 3(a)) primarily facilitates the learning of interpolation and correlation over a short period from noisy data. In contrast, the patchwise method (Fig. 3(b)) fosters an understanding of interactions over extended periods. Inspired by the masked autoencoder approach to video data, each agent's trajectory is divided into non-overlapping patches in space and time given a certain timeframe. The size of these patches is chosen randomly, and patches are masked randomly. The time-based strategy (Fig. 3(c)) simulates scenarios where a sensor might fail abruptly, leading to missing data at random timestamps.

The three tasks - motion prediction, conditional prediction and occlusion handling are three special masking cases (Fig. 2). Each task involves the process of prediction, where future trajectories are treated as unknown and masked out. In conditional motion prediction, alongside the full historical data, the future desired path of the ego vehicle is also provided. For occlusion handling, the input data is often incomplete due to occlusions. Since the three tasks correspond to special cases of masking, they can be carried out by adapting the same network architecture accordingly.

Figure 4: Two examples of labeling occluded objects using ray tracing occupancy grid map from one vehicle’s view. The labeled object track will be used to evaluate the occlusion handling performance. The dark blue occluded agent in the occluded area (in grey grids) is blocked by other visible agents (in cyan), from the ego vehicle’s (in teal) view.

(a) Qualitative results of motion prediction using Autobot with random mask pretrain on Argoverse dataset. The past trajectories of all other vehicles are shown in brown, the past trajectories of ego vehicle are shown in dark blue, the ground-truth trajectories are shown in red, the predicted trajectories are shown in green.

(b) Qualitative results of conditional motion prediction using Autobot with random mask pretrain on Argoverse dataset. Given the ego vehicle’s past (in dark blue) and future (in red) trajectories, and past trajectories of all other vehicles (solid line, one color for one agent), the predicted trajectories of all other agents are shown in the dashed line.

Figure 5: Qualitative results with our random mask pretrain framework.

## Experiments

### V-A Datasets

We evaluate the efficacy of our pretraining framework for motion and conditional prediction on two widely used datasets: Argoverse and nuScenes. Argoverse motion forecasting dataset contains $205,942$ training sequences and $39,472$ validation sequences. Each sequence includes data of all agents' positions over a 5 seconds period at $10{Hz}$. The task is to predict the subsequent 3 seconds' trajectory based on the initial 2 seconds of past observations with HD map information provided. The nuScenes dataset consists of $32,186$ training and $9,041$ validation sequences. The objective, in this case, is to predict future 6 seconds' trajectories at a rate of 2 Hz, given the past 2 seconds' trajectory data.

In order to evaluate our model's proficiency in handling occlusions, we leverage the multi-track INTERACTION dataset. This dataset is collected by drones and potential traffic cameras, which enables the potential to label occluded objects from the perspective of a single vehicle. We auto-labeled occluded objects in the validation dataset based on a randomly designated ego agent. From a bird's-eye view, and given the positions and sizes of all agents, we compute the occupancy grid following. Objects within the occluded region are labeled as occluded, as demonstrated in Fig. 4. The network is initially trained using the original training data, after which it is tested on this postprocessed validation dataset. The training uses a bird's-eye view without occlusions, while the validation set includes realistic real-world occlusions as seen from the vehicle's perspective.

Figure 6: Conditional motion prediction on Argoverse dataset. Pretraining with fine-tuning is more accurate than training from scratch. The model is Autobot-joint. X-axis represents relative wall training time (4×A100 GPUs), and Y-axis represents the m i n A D E6. The pretraining is done with 75% pointwise masking.

### V-B Masking Strategy

We have conducted extensive testing to assess the impact of different masking strategies on performance. The results of these ablation experiments are presented in Table I. Table I(a) displays the outcomes of tests utilizing varying mask ratios and profiles for the pretraining task. Interestingly, for pointwise masking, ratios of 50% and 75% yielded superior results. Conversely, for both patchwise and time-only masks, a 25% ratio demonstrated the best performance. Among the tested profiles, point masking proved most effective. In regards to frozen encoder weights, the experiment shows that the unfrozen encoder achieves better results (Table I(b)). We also test with different encoder sizes. The default Autobot model utilizes 2 sets of axial attention for temporal and social relations ($\sim$`<!-- -->`{=html}1,160,320 parameters for the encoder). Despite extending the size to include 4 and 6 sets, larger networks did not result in improved performance as demonstrated in Table I(c). This could be attributed to the Argoverse1 dataset size which is not large.

To ensure fair comparison between pretraining and training from scratch, we perform experiments over comparable time periods and on identical devices. As an example, the conditional motion prediction results for Argoverse dataset (Fig. 6) show that pretraining achieves better results and converges faster. Our experiments also show that it can learn other tasks from that same pretrained network at a faster rate and to better results.

Method minADE_5 ↓ minADE_10 ↓ Miss Rate↓ (Top 5) GOHOME 1.42 1.15 0.57 THOMAS 1.33 1.04 0.55 PGP 1.27 0.94 0.52 FRM 1.18 0.88 0.48 Autobot (Baseline, w/o ensemble) 1.43 1.05 0.66 Autobot w/ [P] (Ours) 1.38 (3.5%) 0.98 (6.7%) 0.60 (9.1%) TABLE II: Performance comparison of different models on nuScenes dataset. Here we use the baseline results of Autobot without ensemble to maintain a fair comparison.

TABLE III: Prediction performance of different models on Argoverse validation dataset. Note that the results presented have been obtained from our own training runs.

TABLE IV: Conditional motion prediction results for Argoverse and nuScenes validation data.

TABLE V: Prediction results for the postprocessing INTERACTION validation dataset, focusing on scenarios with occlusion.

### V-C Motion Prediction

We have integrated our framework into the nuScenes (Table II) and Argoverse (Table III) datasets for motion prediction. The results indicate that the implementation of random masking pretraining enhances performance. In nuScenes, our approach achieves comparable results to other state-of-the-art methods. Compared to the baseline, the application of random masking showed marked improvements in the metrics including $minADE_{5}$, $minADE_{10}$ and miss rate for the Top 5 in 2 meters, with percentage decreases of 3.5% and 6.7% and 9.1% respectively. Note that in order to maintain a fair comparison, the Autobot baseline we utilize does not include ensemble operations, as these are not used in our post-processing steps. In Argoverse, we incorporate two methods- Autobot-joint and HivT. Both of them show a positive impact of masked pertaining, resulting in an decrease of $minADE_{6}$, $minFDE_{6}$ by 3.9% and 4.6% for Autobot, and 4.9% and 1.6% for HiVT. Note that for HiVT, we prioritized speed and trained on four GPUs, resulting in lower of performance than training on a single GPU. However, our comparison is conducted under the same environment and settings.

### V-D Conditional Motion Prediction

We evaluate conditional motion prediction on nuScenes and Argoverse datasets with Autobot again. Given the history information and the ego vehicle's desired future trajectories, the task is to predict all other agents' possible future trajectories. The results for this task are shown in Table. IV. For Argoverse, it reduces the minADE6 and minFDE6 by 12.0% and 10.2%, respectively. For nuScenes, it reduces minADE10 and minFDE10 by 8.8% and 4.9%. Given that the Argoverse data features higher frequency and more waypoints, it is plausible that random masking exhibits superior performance as the input size expands.

### V-E Occlusion Handling

We use the postprocessed validation INTERACTION dataset to evaluate the efficacy of Autobot in complex scenarios as well as the benefits of random masking. The network is trained with regular INTERACTION training data. However, during the inference time, the network can only access the agent's waypoints annotated as visible. Thus, for the agents that are partially occluded (Section V-A), the network can only see incomplete history. We then measure how the network can capture such partially occluded agents' future trajectories. As shown in Table V, the use of random masking enhances the network's capability to predict the partially occluded agent's future trajectory, with improvements exceeding 30% for both $ADE$ and $FDE$.

The results are not surprising as the pretraining is a sort of random synthetic occlusion (as opposed to the actual realistic occlusions that we model in the validation set). Therefore, the pretrained network has a considerable advantage over a network simply trained with bird's eye view data and no occlusions.

## Conclusion

In this paper, we propose a simple and effective random mask pretraining framework which facilitates the motion prediction task in general and conditional motion prediction. Furthermore, our framework largely improves the prediction accuracy for occlusion scenarios. The self-supervised learning and masked autoencoder can be explored further with state-of-the-art techniques in the field of motion prediction for autonomous driving. Additionally, exploring new auxiliary tasks within the self-supervised learning domain offers exciting possibilities for further advancements. We think that exploring self-supervised learning may be beneficial as the volume of motion prediction data expands.
