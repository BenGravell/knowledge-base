HDMapNet: An Online HD Map Construction and Evaluation Framework

Topics include High-definition map construction, Semantic map learning, Autonomous driving, Bird's-eye view perception, Sensor fusion, Lane detection, Chamfer distance, Vectorized maps, NuScenes, HDMapNet.

Introduces online HD semantic map learning from onboard cameras and LiDAR, with HDMapNet producing bird's-eye-view semantic, instance, and direction predictions that can be converted into vectorized lane dividers, boundaries, and crossings. The paper is especially useful as an early benchmark and metric proposal for learned HD map construction, including semantic- and instance-level evaluations based on raster overlap, Chamfer-style geometry distance, and average precision.

Constructing HD semantic maps is a central component of autonomous driving. However, traditional pipelines require a vast amount of human efforts and resources in annotating and maintaining the semantics in the map, which limits its scalability. In this paper, we introduce the problem of HD semantic map learning, which dynamically constructs the local semantics based on onboard sensor observations. Meanwhile, we introduce a semantic map learning method, dubbed HDMapNet. HDMapNet encodes image features from surrounding cameras and/or point clouds from LiDAR, and predicts vectorized map elements in the bird's-eye view. We benchmark HDMapNet on nuScenes dataset and show that in all settings, it performs better than baseline methods. Of note, our camera-LiDAR fusion-based HDMapNet outperforms existing methods by more than 50% in all metrics. In addition, we develop semantic-level and instance-level metrics to evaluate the map learning performance. Finally, we showcase our method is capable of predicting a locally consistent map. By introducing the method and metrics, we invite the community to study this novel map learning problem.

## Introduction

High-definition (HD) semantic maps are an essential module for autonomous driving. Traditional pipelines to construct such HD semantic maps involve capturing point clouds beforehand, building globally-consistent maps using SLAM, and annotating semantics in the maps. This paradigm, though producing accurate HD maps and adopted by many autonomous driving companies, requires a vast amount of human efforts.

As an alternative, we investigate scalable and affordable autonomous driving solutions, e.g. minimizing human efforts in annotating and maintaining HD maps. To that end, we introduce a novel semantic map learning framework that makes use of on-board sensors and computation to estimate vectorized local semantic maps. Of note, our framework does not aim to replace global HD map reconstruction, instead to provide a simple way to predict local semantic maps for real-time motion prediction and planning.

## Conclusion

HDMapNet predicts HD semantic maps directly from camera images and/or LiDAR point clouds. The local semantic map learning framework could be a more scalable approach than the global map construction and annotation pipeline that requires a significant amount of human efforts. Even though our baseline method of semantic map learning does not produce map elements as accurate, it gives system developers another possible choice of the trade-off between scalability and accuracy.

In this section, we propose evaluation protocols for semantic map learning, including semantic metrics and instance metrics.

Our point cloud encoder $\phi_{P}$ is a variant of PointPillar with dynamic voxelization, which divide the 3d space into multiple pillars and learn feature maps from pillar-wise features of pillar-wise point clouds. The input is $N$ lidar points in the point cloud. For each point $p$, it has three-dimensional coordinates and additional $K$-dimensional features represented as $f_{p} \subseteq {\mathbb{R}}^{K + 3}$.

Tasks & Metrics. We evaluate our approach on the NuScenes dataset. We focus on two sub-tasks: semantic map segmentation and instance detection. Due to the limited types of map elements in the nuScenes dataset, we consider three static map elements: lane boundary, lane divider, and pedestrian crossing.

Figure 1: In contrast to pre-annotating global semantic maps, we introduce a novel local map learning framework that makes...
