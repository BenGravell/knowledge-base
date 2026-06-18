HisTrackMap: Global Vectorized High-Definition Map Construction via History Map Tracking

Topics include High-definition map construction, Vectorized maps, Autonomous driving, Global map construction, Map tracking, Temporal consistency, Historical priors, Bird's-eye view perception, NuScenes, Argoverse 2, HisTrackMap.

Extends online vectorized HD map construction from single-frame local prediction toward temporally consistent global mapping. HisTrackMap explicitly tracks historical map-element trajectories through instance-level history maps, fuses those priors into current track queries, and adds a global geometry metric for evaluating map construction over time.

As an essential component of autonomous driving systems, high-definition (HD) maps provide rich and precise environmental information for auto-driving scenarios; however, existing methods, which primarily rely on query-based detection frameworks to directly model map elements or implicitly propagate queries over time, often struggle to maintain consistent temporal perception outcomes. These inconsistencies pose significant challenges to the stability and reliability of real-world autonomous driving and map data collection systems. To address this limitation, we propose a novel end-to-end tracking framework for global map construction by temporally tracking map elements' historical trajectories. Firstly, instance-level historical rasterization map representation is designed to explicitly store previous perception results, which can control and maintain different global instances' history information in a fine-grained way. Secondly, we introduce a Map-Trajectory Prior Fusion module within this tracking framework, leveraging historical priors for tracked instances to improve temporal smoothness and continuity....

## Introduction

High-definition (HD) maps, which include vectorized map elements such as lane dividers, pedestrian crossings, and road boundaries, play a critical role in the navigation and planning of autonomous driving. Traditional map construction methods use the SLAM-based method to collect offline map data, followed by extensive post-processing to generate HD maps. However, these methods are constrained by significant limitations, including substantial costs, the absence of real-time processing capabilities, and difficulties in accommodating dynamic environments and road updates.

Recent advancements in Perspective View (PV)-to-Bird's-Eye View (BEV) methods have significantly enhanced vectorized HD map construction such as. These approaches leverage the DETR-based detection paradigm \[\] to achieve precise HD map generation. To illustrate the differences across various paradigms. Nevertheless, internal prediction instabilities within the model coupled with uncontrollable environmental factors, such as occlusions or low-light conditions, frequently result in temporal perception inconsistencies, posing substantial challenges for real-world autonomous driving scenarios....

## Conclusion

In this work, we introduce a novel method for end-to-end vectorized HD map construction via tracking history maps, enabling more robust and efficient temporal association modeling. Specifically, the history map is systematically constructed and updated based on past perception results, thereby minimizing redundant computations. We introduce the Map-Trajectory Prior Fusion method, which integrates historical map data with current perception features to improve the precision of frame-to-frame transformations....

Similarly, we perform analogous operations in the Bird's-Eye View space. To ensure that the sampled BEV features $\mathbf{F}_{sampled\_bev}$ incorporate positional information, we introduce a sinusoidal position embedding ${\mathbf{P}\mathbf{E}}_{bev} \in {\mathbb{R}}^{H \times W \times C}$. Then, we utilize $\mathcal{M}_{val}$ to sample BEV feature $\mathbf{F}_{bev}$ through the ${SampledBEV}{( \cdot )}$ function.

### Instance-Level History Maps

G-mAP leverages the strengths of both rasterized and vectorized representations. It consists of two components: rasterization-based mAP for polygons (e.g., pedestrian) and vectorization-based mAP for polylines...
