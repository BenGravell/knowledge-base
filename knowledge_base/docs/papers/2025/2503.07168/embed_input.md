<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HisTrackMap: Global Vectorized High-Definition Map Construction via History Map Tracking

Topics include High-definition map construction, Vectorized maps, Autonomous driving, Global map construction, Map tracking, Temporal consistency, Historical priors, Bird's-eye view perception, NuScenes, Argoverse 2, HisTrackMap.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends online vectorized HD map construction from single-frame local prediction toward temporally consistent global mapping. HisTrackMap explicitly tracks historical map-element trajectories through instance-level history maps, fuses those priors into current track queries, and adds a global geometry metric for evaluating map construction over time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As an essential component of autonomous driving systems, high-definition (HD) maps provide rich and precise environmental information for auto-driving scenarios; however, existing methods, which primarily rely on query-based detection frameworks to directly model map elements or implicitly propagate queries over time, often struggle to maintain consistent temporal perception outcomes. These inconsistencies pose significant challenges to the stability and reliability of real-world autonomous driving and map data collection systems. To address this limitation, we propose a novel end-to-end tracking framework for global map construction by temporally tracking map elements' historical trajectories. Firstly, instance-level historical rasterization map representation is designed to explicitly store previous perception results, which can control and maintain different global instances' history information in a fine-grained way. Secondly, we introduce a Map-Trajectory Prior Fusion module within this tracking framework, leveraging historical priors for tracked instances to improve temporal smoothness and continuity. Thirdly, we propose a global perspective metric to evaluate the quality of temporal geometry construction in HD maps, filling the gap in current metrics for assessing global geometric perception results.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Substantial experiments on the nuScenes and Argoverse2 datasets demonstrate that the proposed method outperforms state-of-the-art (SOTA) methods in both single-frame and temporal metrics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-definition (HD) maps, which include vectorized map elements such as lane dividers, pedestrian crossings, and road boundaries, play a critical role in the navigation and planning of autonomous driving. Traditional map construction methods use the SLAM-based method to collect offline map data, followed by extensive post-processing to generate HD maps. However, these methods are constrained by significant limitations, including substantial costs, the absence of real-time processing capabilities, and difficulties in accommodating dynamic environments and road updates.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advancements in Perspective View (PV)-to-Bird's-Eye View (BEV) methods have significantly enhanced vectorized HD map construction such as. These approaches leverage the DETR-based detection paradigm to achieve precise HD map generation. To illustrate the differences across various paradigms. Nevertheless, internal prediction instabilities within the model coupled with uncontrollable environmental factors, such as occlusions or low-light conditions, frequently result in temporal perception inconsistencies, posing substantial challenges for real-world autonomous driving scenarios. Latent query embedding is used as a stream memory, facilitating the propagation of temporal information within a unified latent memory. Furthermore, MapTracker employs a tracking paradigm that further utilizes query propagation and implicit latent memory to associate instance-level map elements across consecutive frames, enhancing temporal consistency. In such a framework, a Motion MLP proposed is essential for obtaining the next-frame latent memory considering the pose transformation between consecutive frames. Consequently, it employs a transformation loss to guide the Motion MLP, implicitly ensuring the accuracy of the pose transformation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is understood that a substantial amount of historical perception map data generated during vehicle navigation could potentially be leveraged as prior knowledge or utilized to reduce computational overhead in overlapping map regions. However, the current approach of implicit encoding through instance queries remains inadequate for precisely recording or preserving past geometric map information. To fully utilize existing perception results, we propose HisTrackMap, which explicitly maintains instance-level history maps for corresponding map instances under a tracking paradigm. This approach provides prior information for subsequent navigation perception, ensuring smoother and more continuous HD map construction and enhancing the efficiency and accuracy of temporal information propagation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. illustrates the global rasterized map generated from a continuous navigation sequence, along with details of instance tracking. Furthermore, we propose Map-Trajectory Prior Fusion, which leverages the history map to provide refined prior information for track queries at the subsequent timestamp by integrating position-aligned PV and BEV features. Our HisTrackMap leverages instance-level history maps to establish one-to-one correspondences between track queries and map trajectories, thereby enhancing global geometric consistency and constructing a temporally consistent vectorized HD map.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although traditional Chamfer Distance mean Average Precision (mAP) metrics are widely used for HD map construction, we argue that single-frame metrics are insufficient for evaluating performance in practical autopilot scenarios and map data collection processes. For example, they fail to maintain global constructed map consistency across sequential frames, which is critical to ensure robust long-term perception, reliable decision-making, and efficient data acquisition. While MapTracker introduced consistency-aware metrics (C-mAP) to penalize inconsistent map elements, they remain indirect methods of evaluation. To address this issue, we propose a global geometric-aware metric (G-mAP), which directly evaluates the global perceptual quality of the entire scene. The proposed HisTrackMap consistently outperforms existing methods, demonstrating the effectiveness of utilizing history maps compared to implicit transformations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

An end-to-end tracking-enhanced framework, HisTrackMap, for vectorized HD map construction is proposed, which leverages temporal information by maintaining instance-level history maps, reducing redundant computations, and enhancing efficiency.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Map-Trajectory Prior Fusion module is designed to fully utilize the map trajectory information from the history map, combined with instance-level perception features, to provide priors for the corresponding track queries in future frames, thereby optimizing the temporal propagation process.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A novel benchmark with a global geometric perspective is introduced to address the limitations of existing evaluation methods in practical applications. Our HisTrackMap achieves SOTA results in the popular nuScenes and Argoverse 2 datasets.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview Architecture", "weight": 1.0} -->

The encoder extracts perception features (BEV feature $\mathbf{F}_{bev}$ and PV feature $\mathbf{F}_{pv}$) from surrounding-view images to localize spatial structures. The input detection query $\mathbf{Q} \in {\mathbb{R}}^{N_{q} \times C}$ is updated through MapDecoder to produce the coordinates $\mathbf{P} \in {\mathbb{R}}^{N_{q} \times N_{p} \times 2}$, categories $\mathbf{C} \in {\mathbb{R}}^{N_{q} \times 3}$ (pedestrian, boundry, divider) and scores $\mathbf{S} \in {\mathbb{R}}^{N_{q}}$. Here, $N_{q}$ denotes the number of detected queries, $N_{p}$ represents the number of points of a map instance, and $C$ is the feature dimension.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview Architecture", "weight": 1.0} -->

After the decoder, the outputted detected queries and propagated track queries are filtered to be positive using a detection threshold $\tau_{det}$ and a tracking threshold $\tau_{track}$. These positive $N_{track}$ queries $\mathbf{Q}_{track}$ are propagated to the next frame as new track queries. Queries with confidence below the thresholds are treated as disappeared instances and discarded as negative queries. In summary, map instances will be categorized as newly appeared, consistently tracked, or disappeared, and the corresponding history maps will be initialized, updated with the rasterized map, or removed accordingly. Furthermore, the Map-Trajectory Prior Fusion utilizes the history map to sample corresponding positions on perception features extracted by the encoder, establishing a strong geometric prior for initializing track queries in the new frame and explicitly optimizing the propagation of track queries across temporal sequences.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview Architecture", "weight": 1.0} -->

Section 3.2 introduces the instance-level history maps for maintaining and updating historical map trajectories. Subsequently, Section 3.3 presents the Map-Trajectory Prior Fusion, which provides prior information to enrich track queries. Finally, Section 3.4 proposes the metrics to address the current insufficiencies in evaluating stability and continuity in real-world autonomous driving scenarios.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Instance-Level History Maps", "weight": 1.0} -->

We first introduce instance-level maps used for storing historical information. The history map is maintained for the tracked instances generated during online prediction to store their trajectory information. During the propagation process, each track query corresponds to a unique map instance and history map, thereby establishing a strong one-to-one relationship.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Instance-Level History Maps", "weight": 1.0} -->

At the beginning of frame $t$, $\mathcal{M}$ is a collection of history maps corresponding to a series of track queries, defined as $\mathcal{M}^{t} = {\{\mathbf{M}_{i}^{t}\mid{i = {1,2,\ldots,N_{track}^{t - 1}}}\}}$. Here, each $\mathbf{M}_{i}^{t} \in {\mathbb{R}}^{H \times W}$ indicates the rasterized history map of the $i$-th instance among the $N_{track}^{t - 1}$ instances that have been tracked at the previous frame, where $H$ and $W$ are equal to the height and width of the BEV feature, respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Instance-Level History Maps", "weight": 1.0} -->

Subsequently, the perception results at timestamp $t$ are used to update the history map. For the $j$-th instance, if it is identified as a newly born instance (i.e., no corresponding tracking index is found, and its confidence score $\mathbf{S}_{j}^{t}$ exceeds the detect threshold $\tau_{det}$), the rasterization method ${Raster}{( \cdot )}$ is employed to transform the vectorized map representation $\mathbf{P}_{j}^{t}$ into a rasterized format. The rasterized result is scaled by $\mathbf{S}_{j}^{t}$ to initialize its history map. If the instance has been tracked (i.e., some tracking index is associated, and $\mathbf{S}_{j}^{t}$ exceeds the tracking threshold $\tau_{track}$), the corresponding historical map $\mathbf{M}_{i}^{t - 1}$ is retrieved based on its tracking index $i$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Instance-Level History Maps", "weight": 1.0} -->

This history map is then temporally decayed using a decay factor $\lambda$ and updated with the newly rasterized result, yielding the updated history map. After completing the update process, the history map $\mathbf{M}_{i}^{t}$ is finalized. At timestamp $t$, both the total number of tracked instances $N_{track}^{t}$ and the collection of history maps $\mathcal{M}^{t}$ are updated accordingly. At the $t + 1$ timestamp, if the confidence score exceeds the threshold $\tau_{track}$, the instance will continue to be tracked. At timestamp t+1, $\mathcal{M}^{t}$ is dynamically aligned with the updated ego position to obtain warped history maps $\mathcal{M}_{w}^{t + 1}$, thereby enabling initialization for the subsequent timestamp.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Instance-Level History Maps", "weight": 1.0} -->

Note that, if the prediction confidence of some track query is below the $\tau_{track}$, it indicates that that instance has disappeared or has not been successfully tracked at the current frame. Consequently, it is necessary to remove the corresponding track query and history map $\mathbf{M}_{r}$ from $\mathcal{M}^{t + 1}$, and the total number of tracked instances $N_{track}^{t + 1}$ will be decremented accordingly.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Instance-Level History Maps", "weight": 1.0} -->

Each map instance follows the process of initialization, tracking, and history map updating to achieve the binding of historical trajectory information with the track query, enabling temporal propagation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

As aforementioned, to address the limitations of implicit temporal propagation in capturing detailed feature transformations during motion, the Map-Trajectory Prior Fusion is designed to integrate historical map trajectory information into track queries, enhancing temporal prior utilization and perceptual consistency. The Map-Trajectory Prior Fusion first samples instance features from the history map within the PV and BEV feature spaces. Since the number of instance features varies, padding is applied to align them to a uniform length. These instance-level perception features are then individually integrated into the track queries through cross-attention.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

Historical information provides both semantic category and spatial trajectory coordinate data. To enhance the semantic representation of track queries, we define an initial class embedding ${\mathbf{C}\mathbf{E}}_{init} \in {\mathbb{R}}^{3 \times C}$, which encodes previous track categories into a class embedding ${\mathbf{C}\mathbf{E}} \in {\mathbb{R}}^{N_{track} \times C}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

The history map is a fine-grained map with temporal decay. Therefore, we generate the valid pixel mask $\mathcal{M}_{val}$ by filtering pixels in $\mathcal{M}$ that exceed the map threshold $\tau_{map}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

Then, we project $\mathcal{M}_{val}$ into the perspective view space using the projection function ${Proj}{( \cdot )}$. In this space, the PV features $\mathbf{F}_{pv}$ are combined with the corresponding positional embedding ${\mathbf{P}\mathbf{E}}_{pv}$ to form enhanced feature representations. Subsequently, the ${SampledPV}{( \cdot )}$ function is applied to sample from these enhanced features, resulting in the final sampled PV features

<!-- chunk {"id": "body-0026", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

Similarly, we perform analogous operations in the Bird's-Eye View space. To ensure that the sampled BEV features $\mathbf{F}_{sampled\_bev}$ incorporate positional information, we introduce a sinusoidal position embedding ${\mathbf{P}\mathbf{E}}_{bev} \in {\mathbb{R}}^{H \times W \times C}$. Then, we utilize $\mathcal{M}_{val}$ to sample BEV feature $\mathbf{F}_{bev}$ through the ${SampledBEV}{( \cdot )}$ function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

Next, the PV and BEV features corresponding to each instance, including the historical map trajectories, have been obtained. The track queries, along with their associated sampled features $\mathbf{F}_{sampled\_bev}$ and $\mathbf{F}_{sampled\_pv}$, are then utilized within a cross-attention ${CA}{( \cdot )}$ to finalize the initialization of the track queries for the current timestamp.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

Finally, we explicitly leverage historical trajectories to provide precise priors for track queries, avoiding redundant auxiliary supervision and inaccurate temporal transformations in implicit propagation. Notably, since the valid pixels for each instance vary, we pad the features and apply a padding mask to ensure that each track query focuses on its corresponding positions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Map-Trajectory Prior Fusion", "weight": 1.0} -->

0: Distance cost matrix CM, average confidence scores AS, distance threshold τd i s = {0.25, 0.5, 0.75, 1.0}, valid threshold τv a l i d = 2
0: True positives TP, false positives FP
3: gt_covered ← zeros(CM.shape,dtype=bool)
7: if CM [i] [j] ≤ τd i s and gt_covered[j]==False then
9: TP [i] ← TP [i] + 1 // Match multiple ground truth instances
12: else if CM [i].min &gt; τd i s + τv a l i d then
14: else if CM [i].min ≤ τd i s + τv a l i d then
Algorithm 1 Global_Instance_Match

<!-- chunk {"id": "body-0030", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

Current map construction metrics have the following limitations: Single-frame mAP does not adequately capture the overall quality of a map, as it emphasizes local and instantaneous evaluations while neglecting the assessment of continuity and consistency. consistency-aware C-mAP indirectly addresses consistency but does not explicitly evaluate map completeness. To address these, we propose a global geometric-aware metric (G-mAP) that evaluates construction quality from a global perspective.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

First, the vectorized ground truth elements $\mathbf{P}_{local}^{gt}$ from $N_{seq}$ single frames of a sequence segment are projected into a global coordinate system and rasterized to produce a complete global map containing all map instances $\mathbf{P}_{global}^{gt}$ as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

where ${RasterGlobal}{( \cdot )}$ denotes the process of transforming local coordinates into the global coordinate system and performing rasterization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

To address truncation issues of polygons (e.g., pedestrians) during vehicle motion, it is more effective to evaluate them using IoU metrics. Thus, we adopt the rasterization-based mAP to evaluate closed pedestrian masks with $AP_{polygon}$. For polyline categories, we use the Merge function ${Merge}{( \cdot )}$ to combine the tracking results $\mathbf{P}_{local}^{pred}$ from each frame, obtaining a globally complete instance vector $\mathbf{P}_{global}^{pred}$ as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

To obtain the vector representation of the entire instance, the ground truth mask of the corresponding instance is utilized to extract discrete points via Farthest Point Sampling, enabling the fitting of the complete polyline. Subsequently, the $AP_{polyline}$ is calculated using the Chamfer Distance metric.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

G-mAP leverages the strengths of both rasterized and vectorized representations. It consists of two components: rasterization-based mAP for polygons (e.g., pedestrian) and vectorization-based mAP for polylines (e.g., divider and boundary). By averaging the results across the three categories, G-mAP achieves a comprehensive evaluation from a global geometric perspective.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

The ${Global}\_{Instance}\_{Match}$ function is used to obtain false positives (FP) and true positives (TP) under the Chamfer Distance metric. We construct a distance cost matrix ${\mathbf{C}\mathbf{M}} \in {\mathbb{R}}^{N_{pred} \times N_{gt}}$ using $N_{pred}$ predictions and $N_{gt}$ ground truths, which represents the average distance between the predicted point coordinates and the ground truth for each instance. Additionally, we compute the average confidence scores ${\mathbf{A}\mathbf{S}} \in {\mathbb{R}}^{N_{pred}}$ for each instance and define a distance threshold $\tau_{dis}$ to evaluate the vectorization-based mAP across different thresholds. It is worth noting that we have optimized the evaluation algorithm due to the unique characteristics of the global perspective.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Global Geometric HD Mapping Evaluation", "weight": 1.0} -->

As shown in Algorithm, to prevent overlooking shorter instances that have been accurately identified, our algorithm permits predicted instances to correspond to multiple shorter ground truth instances in the global perspective by incrementing the true positive (TP) count. In addition, there are instances in practice that have been perceived but not labelled. To address this issue, we use a validity threshold $\tau_{valid}$ to constrain the counting of false positives (FP).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Settings", "weight": 1.0} -->

Dataset. We evaluate HisTrackMap on two popular autonomous driving datasets: nuScenes and Argoverse 2. The nuScenes dataset contains 1,000 scenes, each spanning 20 seconds, with data from six synchronized RGB cameras and detailed pose information. The Argoverse 2 dataset includes 1,000 sequences with high-resolution images from seven ring cameras, two stereo cameras, LiDAR point clouds, and map-aligned 6-DoF pose data. Experiments were conducted on both the old and new dataset splits for comprehensive evaluation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Settings", "weight": 1.0} -->

Metrics. Following previous work, we adopt mean Average Precision (mAP) as the primary evaluation metric. Evaluation thresholds are set at 0.5m, 1.0m, and 1.5m. $AP_{ped}$, $AP_{div}$, and $AP_{bou}$ represent average precision for pedestrians, dividers, and boundaries, respectively. In addition, we employ consistency-aware metric (C-mAP) and further introduce a novel global geometric-aware augmented metric (G-mAP), as detailed in Sec. 3.4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Settings", "weight": 1.0} -->

Implementation Details. Our framework builds on MapTracker, which serves as the primary baseline. We removed the Motion MLP and the auxiliary transformation loss used for its supervision while keeping other loss functions consistent with MapTracker. Training on the nuScenes dataset was conducted on 8 NVIDIA RTX A100 GPUs for 72 epochs across three stages (18, 6, and 48 epochs). Similarly, we trained on the Argoverse2 dataset for 35 epochs (12, 3, and 20 epochs) to align with MapTracker. Additionally, to ensure alignment with methods such as MapTR, we evaluated a shorter 24-epoch training configuration on both datasets. To address inaccuracies in the PV projection caused by the dataset's missing Z-axis coordinates, we introduced a complete Map-Trajectory Prior Fusion in Stage 2 to accelerate model convergence. In Stage 3, we exclusively adopted a single BEV Prior to further enhancing model performance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparision with SOTA Method", "weight": 1.0} -->

Comparison on nuScenes. As shown in Table, we compare HisTrackMap with state-of-the-art methods. HisTrackMap demonstrates superior performance at 24 epochs, achieving 73.8 mAP, outperforming MapTracker, which achieves 71.9 mAP, by +1.9 mAP. In addition, HisTrackMap achieves 64.7 C-mAP and 48.5 G-mAP, outperforming MapTracker by +1.3 C-mAP and +1.2 G-mAP, respectively. In the 72-epoch experiment, HisTrackMap achieved 76.6 mAP, 68.7 C-mAP, and 50.2 G-mAP respectively. Furthermore, recent methods like Mask2Map and MGMap use single-frame frameworks with limited temporal modeling, while HisTrackMap outperforms them in all metrics. Notably, by removing transformation loss supervision of Motion MLP, HisTrackMap achieves about 20% faster training than MapTracker.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparision with SOTA Method", "weight": 1.0} -->

During inference, HisTrackMap runs at 10.3 FPS, slightly slower than MapTracker's 10.9 FPS due to feature sampling overhead, which could be optimized with parallel acceleration in practical applications. In summary, HisTrackMap improves performance and remains practical for real-time autonomous driving applications.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparision with SOTA Method", "weight": 1.0} -->

Comparison on Argoverse 2. The results on the Argoverse 2 dataset, as presented in Table, further validate the effectiveness of HisTrackMap. In the 24-epoch experiment, HisTrackMap achieves a notable mAP improvement of +8.5 over HRMapNet and +9.4 over MapTRv2. Additionally, HisTrackMap surpasses MapTracker with +1.2 mAP, +3.5 C-mAP, and +0.8 G-mAP at 24 epochs, and +0.9 mAP, +1.2 C-mAP, and +0.6 G-mAP at 35 epochs. Note that due to the different sampling intervals of HisTrackMap and MapTracker on the Argoverse 2 dataset compared to the other methods, we can only evaluate the mAP metrics.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparision with SOTA Method", "weight": 1.0} -->

Comparison on non-overlapping datasets. The nuScenes and Argoverse 2 datasets exhibit geographical overlaps. StreamMapNet proposes a non-overlapping dataset split for them. The experimental results are shown in Table. Our method surpasses MapTracker, achieving improvements of +1.2 mAP, +0.3 C-mAP, and +0.5 G-mAP on nuScenes, and +1.1 mAP, +1.4 C-mAP, and +0.9 G-mAP on Argoverse 2. We conducted cross-dataset experiments to demonstrate further the superior generalization of HisTrackMap. The encoder and decoder were initialized with weights from nuScenes and Argoverse 2 respectively, and finetuned for 12 epochs on the nuScenes newsplit before testing. HisTrackMap achieved 44.5 mAP, 35.1 C-mAP, and 31.2 G-mAP, demonstrating superior generalization performance over MapTracker.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quantitative Evaluations", "weight": 1.0} -->

Fig. presents a qualitative comparison between HisTrackMap and other methods on nuScenes dataset. We utilized the integration of per-frame vectorized HD maps into a global vectorized HD map for better visualization. The rectangular regions highlight instances where our proposed model exhibits superior perception performance. The orange markings indicate that HisTrackMap accurately identified the two separate boundaries at the turning, whereas MapTracker failed to distinguish them. The blue markings highlight that HisTrackMap achieved continuous and consistent tracking through a complex intersection, whereas MapTracker lost the polyline. The green markings indicate that HisTrackMap fully detected the boundary, while MapTracker captured only the first half. In this green example, all models detected a divider that was not actually annotated, emphasizing the necessity of optimizing false positive (FP) counting in G-mAP. Furthermore, although single-frame MapTRv2 can partially perceive results, the integrated results lack sufficient stability and fail to maintain consistent perception. In general, HisTrackMap delivers more accurate and cleaner results, demonstrating superior performance in terms of overall quality and temporal consistency.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation and Robustness Studies", "weight": 1.0} -->

The proposed Map-Trajectory Prior Fusion consists of three main components: Class Embedding, PV Prior, and BEV Prior. To evaluate the contributions of each component, we conducted an ablation study on the nuScenes dataset. The experiment without Map-Trajectory Prior Fusion is used as the baseline. There are several observations from the results. First, introducing Class Embedding improved mAP by 0.7, demonstrating the effectiveness of semantic category priors. Second, incorporating PV Prior and BEV Prior based on Class Embedding further improves mAP from 72.3 to 72.9 and 73.3, respectively. This reveals that it is beneficial to utilize geometric trajectory information to enhance track queries. Third, with the complete Map-Trajectory Prior Fusion, the model achieved the highest 73.8 mAP, highlighting the significance of history map based trajectory priors in effectively leveraging temporal-spatial information to enhance perception performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation and Robustness Studies", "weight": 1.0} -->

The update of the history map primarily relies on the vehicle's motion pose parameters. To evaluate the robustness of HisTrackMap to localization errors, we conducted additional experiments on the nuScenes dataset. Random noise was introduced to the translation and rotation of the extrinsic matrix to disrupt the history map update. The results show that the model achieves 73.0 mAP under noise levels of 0.2 m and 0.02 rad and 73.4 mAP under real-world noise levels (0.1 m, 0.01 rad), maintaining a clear advantage. The experimental results continue to outperform most previous single-frame models, demonstrating the practical effectiveness of HisTrackMap.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduce a novel method for end-to-end vectorized HD map construction via tracking history maps, enabling more robust and efficient temporal association modeling. Specifically, the history map is systematically constructed and updated based on past perception results, thereby minimizing redundant computations. We introduce the Map-Trajectory Prior Fusion method, which integrates historical map data with current perception features to improve the precision of frame-to-frame transformations. Additionally, we propose a global geometric HD mapping evaluation framework that focuses on assessing overall map construction quality. This evaluation is vital for both autonomous driving systems and map data collection processes. In the future, it is desired to extend the current work by exploring a more robust, reliable, and adaptive perception system considering the existence of vehicle localization errors.
