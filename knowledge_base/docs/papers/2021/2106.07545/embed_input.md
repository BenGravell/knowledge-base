PolarStream: Streaming Lidar Object Detection and Segmentation with Polar Pillars

Recent works recognized lidars as an inherently streaming data source and showed that the end-to-end latency of lidar perception models can be reduced significantly by operating on wedge-shaped point cloud sectors rather then the full point cloud. However, due to use of cartesian coordinate systems these methods represent the sectors as rectangular regions, wasting memory and compute. In this work we propose using a polar coordinate system and make two key improvements on this design. First, we increase the spatial context by using multi-scale padding from neighboring sectors: preceding sector from the current scan and/or the following sector from the past scan. Second, we improve the core polar convolutional architecture by introducing feature undistortion and range stratified convolutions. Experimental results on the nuScenes dataset show significant improvements over other streaming based methods. We also achieve comparable results to existing non-streaming methods but with lower latencies. The code and pretrained models are available at.

## Introduction

The ability to accurately perceive objects in dense urban environments still remains a challenging problem for self-driving cars. While such self-driving cars typically deploy a wide variety of sensors lidars play a key role due to the accurate range information provided. Driven in part by the availability of benchmark datasets, the last decade has seen tremendous progress in lidar based 3D object detection. However, these methods all ignore the fact that most lidar sensors scan the scene sequentially as the lidar rotates around the z-axis....

First, Han et al. and then STROBE recognized this problem and proposed solutions which processed lidar sectors (shown in Fig. 1) as soon as they arrived. They showed that a streaming based architecture can achieve significantly reduced latency over the traditional non-streaming baselines. Both of these methods encode the point clouds as an image in bird's-eye view (BEV) using cuboid-shaped voxels. In doing so, they ignore the natural polar representation formed by the lidar sectors. Using cuboid-shaped voxels restricts them to performing convolutions on the minimal rectangular

## Conclusion

In this work we propose a streaming model for simultaneous 3D object Detection, Lidar Segmentation and Panoptic Segmentation. Polar pillars is introduced as a more compact representation for lidar sectors compared to previous methods. Multi-scale context padding including trailing-edge padding and bidirectional padding is proposed to enhance spatial context of the streaming model with minimal latency. Additionally we make several improvements, Feature Undistortion and Range Stratified Convolution& Normalization, to address the problem of applying convolutions on a polar grid....

### Multi-Scale Context Padding

To extend PointPillars for segmentation, we add a semantic segmentation head in parallel with the detection heads. The segmentation head is made of a single 1x1 convolution layer. The input for the segmentation head is concatenation of the outputs from pillar feature encoder and bilinearly upsampled features from the 2D backbone.

### Baselines

Figure 1: Left: An illustration of streaming lidar point clouds on bird’s eye view. Lidar point clouds arrive as wedge-shape sectors (shown in gray masks) as the scanner rotates. Previous methods, Han et al....
