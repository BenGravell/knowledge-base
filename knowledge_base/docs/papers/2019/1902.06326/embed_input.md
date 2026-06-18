PIXOR: Real-time 3D Object Detection from Point Clouds

We address the problem of real-time 3D object detection from point clouds in the context of autonomous driving. Computation speed is critical as detection is a necessary component for safety. Existing approaches are, however, expensive in computation due to high dimensionality of point clouds. We utilize the 3D data more efficiently by representing the scene from the Bird's Eye View (BEV), and propose PIXOR, a proposal-free, single-stage detector that outputs oriented 3D object estimates decoded from pixel-wise neural network predictions. The input representation, network architecture, and model optimization are especially designed to balance high accuracy and real-time efficiency. We validate PIXOR on two datasets: the KITTI BEV object detection benchmark, and a large-scale 3D vehicle detection benchmark. In both datasets we show that the proposed detector surpasses other state-of-the-art methods notably in terms of Average Precision (AP), while still runs at >28 FPS.

## Introduction

Over the last few years we have seen a plethora of methods that exploit Convolutional Neural Networks to produce accurate 2D object detections, typically from a single image. However, in robotics applications such as autonomous driving we are interested in detecting objects in 3D space. This is fundamental for motion planning in order to plan a safe route.

Recent approaches to 3D object detection exploit different data sources. Camera based approaches utilize either monocular or stereo images. However, accurate 3D estimation from 2D images is difficult, particularly in long ranges. With the popularity of inexpensive RGB-D sensors such as Microsoft Kinect, Intel RealSense and Apple PrimeSense, several approaches that utilize depth information and fuse them with RGB images have been developed. They have been shown to achieve significant performance gains over monocular methods....

## Conclusion

In this paper we propose a real-time 3D object detector called PIXOR that operates on LIDAR point clouds. PIXOR is a single-stage, proposal-free, dense object detector that achieve extreme simplicity in the context of 3D object localization for autonomous driving. PIXOR takes bird's eye view representation as input for efficiency in computation. We evaluate PIXOR on the challenging KITTI benchmark as well as a large-scale vehicle detection dataset TOR4D, and show that it outperforms the other methods by a large margin in terms of Average Precision (AP), while still runs at $> 28$ FPS.

### Implementation Details

One direct solution is to use fewer pooling layers. However, this will decrease the size of the receptive field of each pixel in the final feature map, which limits the representation capacity. Another solution is to use dilated convolutions. However, this would lead to checkerboard artifacts in high-level feature maps. Our solution is simple, we use $16 \times$ downsampling factor, but make two modifications. First, we add more layers with a smaller channel number in lower levels to extract more fine-detail information....

Figure 5: Three versions of header network architectures.

Different forms of point cloud representation have been explored in the context of 3D object detection. The main idea is to form a structured representation where standard convolution operation can be applied....
