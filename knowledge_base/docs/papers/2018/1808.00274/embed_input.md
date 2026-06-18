Multimotion Visual Odometry (MVO): Simultaneous Estimation of Camera and Third-Party Motions

Estimating motion from images is a well-studied problem in computer vision and robotics. Previous work has developed techniques to estimate the motion of a moving camera in a largely static environment (e.g., visual odometry) and to segment or track motions in a dynamic scene using known camera motions (e.g., multiple object tracking). It is more challenging to estimate the unknown motion of the camera and the dynamic scene simultaneously. Most previous work requires a priori object models (e.g., tracking-by-detection), motion constraints (e.g., planar motion), or fails to estimate the full SE motions of the scene (e.g., scene flow). While these approaches work well in specific application domains, they are not generalizable to unconstrained motions. This paper extends the traditional visual odometry (VO) pipeline to estimate the full SE motion of both a stereo/RGB-D camera and the dynamic scene. This multimotion visual odometry (MVO) pipeline requires no a priori knowledge of the environment or the dynamic objects. Its performance is evaluated on a real-world dynamic dataset with ground truth for all motions from a motion capture system.

## Introduction

Visual navigation is an important area of research in robotics. Visual odometry (VO) estimates the motion of a camera (i.e., its egomotion) relative to observed static objects within a scene. These static objects must be accurately segmented from any dynamic noise, and this segmentation itself is an area of research focus. Less research in visual navigation has focused on also analyzing the dynamic regions of the scene that these approaches reject.

MVO applies multimodel fitting techniques (e.g., CORAL ) to the traditional VO pipeline to simultaneously estimate the trajectories of all motions within a scene. Sparse, 3D visual features are decomposed into independent rigid motions and the trajectories of all of these motions, including the egomotion of the camera, are estimated simultaneously (Fig. 1: Simultaneous Estimation of Camera and Third-Party Motions")). This paper demonstrates MVO on a stereo camera, but the technique is applicable to a variety of other 3D sensors, including RGB-D cameras and lidar.

## Discussion

MVO consistently segments and estimates the motions of the camera and the four independent objects when they are fully visible. As is to be expected, the two blocks that partially exited the camera frustum had segmentation failures and higher errors, largely due to incomplete feature tracklets.

Feature distribution is an important factor in the performance of any sparse approach. This problem is exacerbated for dynamic objects that take up a small portion of the scene. Additionally, the appearance of these objects is often more volatile making feature association even more difficult. The algorithm is dependent on the accuracy of the input tracklet set and cannot estimate motions for which there are insufficient features. Feature dropouts and lack of tracklets are therefore significant challenges for this type of pipeline, and the development of more robust feature detection and matching pipelines is an ongoing area of research.

## Conclusion

This paper extends the classic VO pipeline to address the multimotion estimation problem. The multimotion visual odometry (MVO) pipeline segments and estimates *all* rigid motions in a scene. It does so by using feature-tracking, sparse graph segmentation, and multiframe batch motion estimation such that it avoids many of the limitations of other multimotion estimation approaches.
