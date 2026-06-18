Quaternion Based Camera Pose Estimation from Matched Feature Points

Topics include Robustness, Pose estimation, Graphs, Accuracy, Online algorithms.

We present a novel solution to the camera pose estimation problem, where rotation and translation of a camera between two views are estimated from matched feature points in the images. The camera pose estimation problem is traditionally solved via algorithms that are based on the essential matrix or the Euclidean homography. With six or more feature points in general positions in the space, essential matrix based algorithms can recover a unique solution. However, such algorithms fail when points are on critical surfaces (e.g., coplanar points) and homography should be used instead. By formulating the problem in quaternions and decoupling the rotation and translation estimation, our proposed algorithm works for all point configurations. Using both simulated and real world images, we compare the estimation accuracy of our algorithm with some of the most commonly used algorithms. Our method is shown to be more robust to noise and outliers. For the benefit of community, we have made the implementation of our algorithm available online and free.

## Introduction

Many applications in computer vision and robotics require measurements of the rotation and translation (i.e., pose) changes of an object as it moves through an environment. In photogrammetry, for example, by knowing the pose changes of the camera, 3D model of a scene can be constructed from a set of 2D images. In robotics, pose estimated from images can be used for navigation, or fused with other sensor measurements (e.g., IMU and GPS) to increase the reliability and accuracy. Camera pose estimation has further applications in simultaneous localization and mapping (SLAM), autonomous vehicles, and augmented reality.

In this work, we present a novel formulation of the camera pose estimation problem using quaternions and present a solution to estimate the pose under this formulation. Our approach, which we refer to as the Quaternion Estimation (QuEst) algorithm, does not use the homography or essential matrices, and decouples the estimation of rotation and translation. Consequently, common problems such as degeneracy for special 3D point configurations are avoided. We present two methods to recover the rotation from seven and six matched feature points. We then show how the unique correct solution can be detected from among the set of recovered solutions.

The main contributions and benefits of the proposed algorithm can be summarized as follows.

The rest of the paper is organized as follows. We briefly review related approaches in Section II, before we formulate the pose estimation problem using quaternions in Section III. We present the QuEst algorithm in Section IV and evaluate its performance under noise in Section V. In Section IV, we further vet the performance of QuEst using the real world image datasets.

## Conclusion and Future Work

By using quaternion representation of rotation, we formulated the camera pose estimation problem and presented the QuEst algorithm to recover the relative pose between two camera views. Unlike the existing homography or essential matrix based methods, QuEst decouples the rotation and translation estimation, and recovers the pose correctly for both cases of general and coplanar points. QuEst can be used to initialize the bundle adjustment algorithm in applications such as SLAM without needing to resort to heuristic methods to detect the coplanarity of the points.
